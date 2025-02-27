import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                for row in range(i, len(matrix)):
                    for col in range(j, len(matrix[0])):
                        if row == i and col == j:
                            continue
                        if matrix[row][col] != 1:
                            break
                        else:
                            count += 1
    return count