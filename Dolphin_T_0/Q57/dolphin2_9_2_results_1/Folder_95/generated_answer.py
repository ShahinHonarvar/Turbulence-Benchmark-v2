import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    H, W = matrix.shape
    for i in range(H):
        for j in range(W):
            for h in range(i + 1, H):
                for w in range(j + 1, W):
                    if matrix[i:h + 1, j:w + 1].sum() == 19:
                        submatrices.append(matrix[i:h + 1, j:w + 1])
    return submatrices