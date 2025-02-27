import numpy as np

def submatrix_with_particular_sum(matrix):
    h, w = matrix.shape
    res = []
    for y in range(h):
        for x in range(w):
            for size_h in range(1, h - y + 1):
                for size_w in range(1, w - x + 1):
                    if np.sum(matrix[y:y + size_h, x:x + size_w]) == -308:
                        res.append(matrix[y:y + size_h, x:x + size_w])
    return res