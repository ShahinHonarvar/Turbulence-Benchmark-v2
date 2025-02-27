import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            p1, p2 = ((i, j), (i, j))
            while p1[0] < matrix.shape[0] and p2[1] < matrix.shape[1]:
                submatrix = matrix[p1[0]:p2[0] + 1, p1[1]:p2[1] + 1]
                if np.sum(submatrix) == 64:
                    result.append(submatrix)
                p1 = (p1[0] + 1, p1[1] + 1)
                p2 = (p2[0] + 1, p2[1] + 1)
    return result