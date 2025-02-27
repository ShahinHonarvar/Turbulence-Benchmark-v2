import numpy as np

def submatrix_with_n_numbers(matrix):
    row, col = matrix.shape
    sub_count = 0
    for i in range(row - 2):
        for j in range(col - 2):
            submatrix = matrix[i:i + 3, j:j + 3]
            if np.count_nonzero(submatrix == 33) == 9:
                sub_count += 1
    return sub_count