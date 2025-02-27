import numpy as np

def submatrix_with_n_numbers(matrix):
    shape = matrix.shape
    if shape[0] * shape[1] < 99:
        return 0
    count = 0
    for i in range(0, shape[0] - 2):
        for j in range(0, shape[1] - 2):
            submatrix = matrix[i:i + 3, j:j + 3]
            count += np.count_nonzero(submatrix == 99) == 9
    return count