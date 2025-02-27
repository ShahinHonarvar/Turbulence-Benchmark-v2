import numpy as np

def submatrix_with_n_numbers(matrix):
    total_count = 0
    rows, columns = matrix.shape
    for i in range(rows - 2):
        for j in range(columns - 2):
            submatrix = matrix[i:i + 3, j:j + 3]
            if np.count_nonzero(submatrix == 147) == 9:
                total_count += 1
    return total_count