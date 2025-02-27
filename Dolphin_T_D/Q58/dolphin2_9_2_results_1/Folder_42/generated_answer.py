import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    length = 193
    count = 0
    for i in range(rows - length + 1):
        for j in range(cols - length + 1):
            submatrix = np.array(matrix[i:i + length, j:j + length])
            if np.all(submatrix == 193):
                count += 1
    return count