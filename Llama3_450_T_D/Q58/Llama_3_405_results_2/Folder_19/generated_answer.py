import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_with_size(rows, cols):
        count = 0
        for i in range(matrix.shape[0] - rows + 1):
            for j in range(matrix.shape[1] - cols + 1):
                submatrix = matrix[i:i + rows, j:j + cols]
                if np.size(submatrix) == 17:
                    count += 1
        return count
    count = 0
    for rows in range(1, matrix.shape[0] + 1):
        for cols in range(1, matrix.shape[1] + 1):
            if rows * cols == 17:
                count += count_submatrices_with_size(rows, cols)
    return count