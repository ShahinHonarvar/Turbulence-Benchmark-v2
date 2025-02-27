import numpy as np

def submatrix_with_n_numbers(matrix):
    matrix = np.array(matrix)
    m, n = matrix.shape
    num_submatrices = 0
    submatrix_size = 51
    for i in range(m - submatrix_size + 1):
        for j in range(n - submatrix_size + 1):
            sub_matrix = matrix[i:i + submatrix_size, j:j + submatrix_size]
            if np.prod(sub_matrix == 51) == 1:
                num_submatrices += 1
    if num_submatrices == 0:
        return 0
    else:
        return num_submatrices