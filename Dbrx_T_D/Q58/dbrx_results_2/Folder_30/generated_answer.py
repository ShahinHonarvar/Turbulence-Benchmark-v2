import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_with_n_numbers(submatrix, n):
        return np.sum(submatrix == n)
    height, width = matrix.shape
    submatrix_count = 0
    for i in range(height - 3):
        for j in range(width - 3):
            submatrix = matrix[i:i + 4, j:j + 4]
            if count_submatrices_with_n_numbers(submatrix, 94) == 16:
                submatrix_count += 1
    return submatrix_count