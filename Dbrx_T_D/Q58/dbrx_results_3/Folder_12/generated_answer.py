import numpy as np

def submatrix_with_n_numbers(matrix):
    submatrices_46 = 0
    for i in range(matrix.shape[0] - 4):
        for j in range(matrix.shape[1] - 6):
            if np.sum(matrix[i:i + 5, j:j + 7]) == 46 * 5 * 7:
                submatrices_46 += 1
    return submatrices_46