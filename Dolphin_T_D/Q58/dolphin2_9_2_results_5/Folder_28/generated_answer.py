import numpy as np

def submatrix_with_n_numbers(matrix):
    shape = np.array(matrix.shape)
    if shape[0] * shape[1] % 37 != 0:
        return 0
    count = 0
    for i in range(shape[0]):
        for j in range(shape[1]):
            if i + 37 <= shape[0] and j + 37 <= shape[1]:
                submatrix = np.array(matrix[i:i + 37, j:j + 37])
                if np.count_nonzero(submatrix) == 37:
                    count += 1
    return count