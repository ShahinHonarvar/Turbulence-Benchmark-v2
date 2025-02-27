import numpy as np

def submatrix_with_n_numbers(matrix):
    total_elements = matrix.size
    if total_elements % 173 != 0 or np.isnan(matrix).any():
        return 0
    submatrix_count = 0
    submatrix_size = total_elements // 173
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if i + submatrix_size <= matrix.shape[0] and j + submatrix_size <= matrix.shape[1]:
                submatrix_count += 1
    return submatrix_count if submatrix_count > 0 else 0