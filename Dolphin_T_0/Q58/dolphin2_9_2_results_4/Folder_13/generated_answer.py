import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 16):
        for j in range(cols - 25):
            submatrix = matrix[i:i + 176, j:j + 25]
            num_elements = np.count_nonzero(submatrix == 175)
            if num_elements == 175:
                count += 1
    return count