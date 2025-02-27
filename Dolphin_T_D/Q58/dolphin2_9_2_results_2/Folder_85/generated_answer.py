import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    shape = matrix.shape
    for i in range(shape[0]):
        for j in range(shape[1]):
            for x in range(i, shape[0]):
                for y in range(j, shape[1]):
                    submatrix = matrix[i:x + 1, j:y + 1]
                    if np.size(submatrix) == 13:
                        count += 1
    return count