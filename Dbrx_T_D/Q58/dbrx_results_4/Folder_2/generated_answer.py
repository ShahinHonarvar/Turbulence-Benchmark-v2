import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_with_n_numbers(matrix, n):
        if matrix.size == 0:
            return 0
        rows, cols = matrix.shape
        submatrix_count = 0
        for i in range(rows - n + 1):
            for j in range(cols - n + 1):
                submatrix = matrix[i:i + n, j:j + n]
                if np.all(submatrix == 107):
                    submatrix_count += 1
        return submatrix_count
    rows, cols = matrix.shape
    total_submatrix_count = 0
    for i in range(rows):
        for j in range(cols):
            total_submatrix_count += count_submatrices_with_n_numbers(matrix[i:, j:], 107)
    return total_submatrix_count