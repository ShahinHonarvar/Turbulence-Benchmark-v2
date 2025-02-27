import numpy as np

def find_all_submatrices(matrix):
    result = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for k in range(i + 1, matrix.shape[0] + 1):
                for l in range(j + 1, matrix.shape[1] + 1):
                    submatrix = matrix[i:k, j:l]
                    result.append((i, j, k, l, np.sum(submatrix)))
    return result

def submatrix_with_particular_sum(matrix):
    result = []
    submatrices = find_all_submatrices(matrix)
    for submatrix in submatrices:
        if submatrix[4] == -336:
            result.append(submatrix[:4].tolist())
    return result