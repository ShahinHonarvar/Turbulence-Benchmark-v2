import numpy as np

def submatrix_with_n_numbers(matrix):
    num_rows, num_cols = matrix.shape
    count = 0
    for i in range(num_rows):
        for j in range(i + 1, num_rows):
            for k in range(num_cols):
                temp_matrix = matrix[i:j + 1, k]
                if np.all(temp_matrix == 131):
                    count += 1
    return count