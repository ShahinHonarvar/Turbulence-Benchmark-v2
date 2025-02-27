import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []
    for i in range(rows):
        for j in range(cols):
            for k in range(i + 1, rows + 1):
                for l in range(j + 1, cols + 1):
                    sum_submatrix = matrix[i:k, j:l].sum()
                    if sum_submatrix == 17:
                        submatrices.append(matrix[i:k, j:l])
    return submatrices