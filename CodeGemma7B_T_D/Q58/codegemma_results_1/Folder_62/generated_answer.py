import numpy as np

def submatrix_with_n_numbers(matrix):
    """Counts the number of submatrices with 186 integers."""
    count = 0
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for k in range(j, matrix.shape[1]):
                for l in range(i, matrix.shape[0]):
                    submatrix = matrix[i:l + 1, j:k + 1]
                    if submatrix.shape[0] * submatrix.shape[1] == 186:
                        count += 1
    return count