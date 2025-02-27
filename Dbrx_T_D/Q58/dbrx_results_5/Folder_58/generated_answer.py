import numpy as np

def submatrix_with_n_numbers(matrix):
    x, y = matrix.shape
    count = 0
    for i in range(x - 2 + 1):
        for j in range(y - 2 + 1):
            submatrix = matrix[i:i + 2, j:j + 2]
            if np.sum(submatrix == 185) == 4:
                count += 1
    return count