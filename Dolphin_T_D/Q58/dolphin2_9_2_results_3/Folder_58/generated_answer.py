import numpy as np

def submatrix_with_n_numbers(matrix, n=185):
    count = 0
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for x in range(i + 1, matrix.shape[0] + 1):
                for y in range(j + 1, matrix.shape[1] + 1):
                    submatrix = matrix[i:x, j:y]
                    if submatrix.size == n:
                        count += 1
    return count