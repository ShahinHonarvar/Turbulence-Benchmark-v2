import numpy as np

def submatrix_with_n_numbers(matrix):
    n = len(matrix)
    m = len(matrix[0])
    count = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 38:
                for row in range(i, n):
                    for col in range(j, m):
                        if sum(matrix[row][col:col + 38]) == 38 * 38:
                            count += 1
                        else:
                            break
    return count