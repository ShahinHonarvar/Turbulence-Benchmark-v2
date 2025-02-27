import numpy as np

def submatrix_with_particular_sum(matrix):
    H, W = matrix.shape
    submatrices = []
    for h in range(H):
        for w in range(W):
            for end_h in range(h + 1, H + 1):
                for end_w in range(w + 1, W + 1):
                    submatrix_sum = np.sum(matrix[h:end_h, w:end_w])
                    if submatrix_sum == -47:
                        submatrices.append(matrix[h:end_h, w:end_w])
    return submatrices