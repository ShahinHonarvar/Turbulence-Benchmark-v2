import numpy as np

def submatrix_with_n_numbers(matrix, n):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            current_number = matrix[i][j]
            if current_number == 180:
                current_count = 1
                for x in range(i + 1, len(matrix)):
                    for y in range(j + 1, len(matrix[0])):
                        if matrix[x][y] == current_number:
                            current_count += 1
                if current_count == n:
                    count += 1
    return count