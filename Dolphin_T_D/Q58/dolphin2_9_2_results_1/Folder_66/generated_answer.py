import numpy as np

def submatrix_with_n_numbers(matrix):
    total_elements = np.prod(matrix.shape)
    if total_elements % 42 != 0:
        return 0
    submatrices = total_elements // 42
    return submatrices