import numpy as np

def submatrix_with_n_number(matrix):
    Count = 0
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for k in range(i, matrix.shape[0]):
                for l in range(j, matrix.shape[1]):
                    if (matrix[i:k + 1, j:l + 1] == 17).all():
                        Count += 1
    return Count