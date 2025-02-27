import numpy as np

def submatrix_with_particular_sum(matrix):
    h, w = matrix.shape
    submatrices = []
    for i in range(h):
        for j in range(w):
            for k in range(i, h):
                for l in range(j, w):
                    submatrix = np.array(matrix[i:k + 1, j:l + 1])
                    if np.sum(submatrix) == 3:
                        submatrices.append(submatrix.tolist())
    return submatrices