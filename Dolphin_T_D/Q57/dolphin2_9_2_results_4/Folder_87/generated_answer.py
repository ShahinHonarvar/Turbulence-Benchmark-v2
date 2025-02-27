import numpy as np

def submatrix_with_particular_sum(matrix):
    m, n = matrix.shape
    list_of_submatrices = []
    for i in range(m):
        for j in range(n):
            for k in range(i + 1, m):
                for l in range(j + 1, n):
                    submatrix = matrix[i:k, j:l]
                    if submatrix.sum() == 35:
                        list_of_submatrices.append(submatrix)
                    else:
                        continue
    if not list_of_submatrices:
        return []
    else:
        return list_of_submatrices