import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for row_i in range(i + 1, matrix.shape[0] + 1):
                for col_j in range(j + 1, matrix.shape[1] + 1):
                    submatrix = matrix[i:row_i, j:col_j].sum()
                    if submatrix == -779:
                        submatrices.append(matrix[i:row_i, j:col_j])
    return submatrices