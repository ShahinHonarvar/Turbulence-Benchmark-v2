import numpy as np

def submatrix_with_particular_sum(matrix):
    num_rows, num_cols = np.shape(matrix)
    submatrices_list = []
    for submatrix_size in range(1, min(num_rows, num_cols) + 1):
        for i in range(0, num_rows - submatrix_size + 1):
            for j in range(0, num_cols - submatrix_size + 1):
                submatrix = matrix[i:i + submatrix_size, j:j + submatrix_size]
                if np.sum(submatrix) == 35:
                    submatrices_list.append(submatrix)
    return submatrices_list