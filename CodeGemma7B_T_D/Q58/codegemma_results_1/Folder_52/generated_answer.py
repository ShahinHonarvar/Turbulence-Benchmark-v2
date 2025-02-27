import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for n in range(matrix.shape[0]):
        for m in range(matrix.shape[1]):
            for x in range(n, matrix.shape[0]):
                for y in range(m, matrix.shape[1]):
                    submatrix = matrix[n:x + 1, m:y + 1]
                    if (submatrix == 147).all():
                        count += 1
    return count