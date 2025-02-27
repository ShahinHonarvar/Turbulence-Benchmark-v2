import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for r in range(i + 1, matrix.shape[0]):
                for c in range(j + 1, matrix.shape[1]):
                    if len(set(matrix[i:r + 1, j:c + 1].flatten())) == 9:
                        count += 1
    return count