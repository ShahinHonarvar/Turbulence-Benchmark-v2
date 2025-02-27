import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    H, W = matrix.shape
    for h in range(H):
        for w in range(W):
            for h2 in range(h, H):
                for w2 in range(w, W):
                    submatrix = matrix[h:h2 + 1, w:w2 + 1]
                    if np.sum(submatrix) == -26:
                        submatrices.append(submatrix)
                        break
    return submatrices