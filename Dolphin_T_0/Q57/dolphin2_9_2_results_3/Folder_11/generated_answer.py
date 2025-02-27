import numpy as np

def submatrix_with_particular_sum(matrix):
    h, w = matrix.shape
    results = []
    for y1 in range(h):
        for x1 in range(w):
            for y2 in range(y1, h):
                for x2 in range(x1, w):
                    submatrix_sum = int(np.sum(matrix[y1:y2 + 1, x1:x2 + 1]))
                    if submatrix_sum == 38:
                        results.append(matrix[y1:y2 + 1, x1:x2 + 1].tolist())
    return results