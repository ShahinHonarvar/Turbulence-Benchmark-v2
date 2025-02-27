import numpy as np

def submatrix_with_n_numbers(matrix):
    size = matrix.shape
    count = 0
    for i in range(size[0]):
        for j in range(size[1]):
            for k in range(i, size[0]):
                for l in range(j, size[1]):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if submatrix.size == 83:
                        count += 1
    return count