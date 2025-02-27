import numpy as np

def submatrix_with_n_numbers(matrix):
    list_of_submatrices = []
    shape = matrix.shape
    m, n = (shape[0], shape[1])
    for i in range(m):
        for j in range(n):
            for k in range(i, m):
                for l in range(j, n):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if len(submatrix) == 159:
                        list_of_submatrices.append(1)
    return len(list_of_submatrices)