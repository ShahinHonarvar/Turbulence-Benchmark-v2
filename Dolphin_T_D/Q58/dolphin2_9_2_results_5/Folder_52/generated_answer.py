import numpy as np

def submatrix_with_n_numbers(matrix):
    size = len(matrix)
    count = 0
    for i in range(size):
        for j in range(size):
            for k in range(i, size):
                for l in range(j, size):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if np.count_nonzero(submatrix) == 147:
                        count += 1
    return count