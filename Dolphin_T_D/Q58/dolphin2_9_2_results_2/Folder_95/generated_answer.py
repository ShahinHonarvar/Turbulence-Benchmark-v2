import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 87:
                for k in range(i, min(rows, i + 3)):
                    for l in range(j, min(cols, j + 3)):
                        if np.sum(matrix[k][l, l + 1, l + 2]) + np.sum(matrix[k + 1][l, l + 1, l + 2]) + np.sum(matrix[k + 2][l, l + 1, l + 2]) == 87 * 3:
                            count += 1
    return count