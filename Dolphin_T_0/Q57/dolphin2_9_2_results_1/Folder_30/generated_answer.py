import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    N_row, N_col = matrix.shape
    for i in range(1, N_row + 1):
        for j in range(1, N_col + 1):
            for x in range(N_row - i + 1):
                for y in range(N_col - j + 1):
                    if np.sum(matrix[x:x + i, y:y + j]) == 21:
                        submatrices.append(matrix[x:x + i, y:y + j])
    return submatrices