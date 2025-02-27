import numpy as np

def submatrix_with_particular_sum(matrix):
    H, W = matrix.shape
    result = []
    for i in range(H):
        for j in range(W):
            for h in range(i + 1, H + 1):
                for w in range(j + 1, W + 1):
                    if sum(matrix[i:h, j:w]) == -863:
                        result.append(matrix[i:h, j:w])
    return result