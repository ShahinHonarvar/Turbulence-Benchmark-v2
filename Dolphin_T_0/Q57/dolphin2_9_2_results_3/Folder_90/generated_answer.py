import numpy as np

def get_submatrices(matrix):
    rows, columns = matrix.shape
    submatrices = []
    for i in range(rows):
        for j in range(columns):
            for k in range(i, rows):
                for l in range(j, columns):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    submatrices.append(submatrix)
    return submatrices

def submatrix_with_particular_sum(matrix):
    submatrices = get_submatrices(matrix)
    result = [submatrix for submatrix in submatrices if np.sum(submatrix) == -452]
    return result