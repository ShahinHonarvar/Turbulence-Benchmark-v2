import numpy as np

def submatrix_with_particular_sum(matrix):
    results = []
    for r in range(matrix.shape[0]):
        for c in range(matrix.shape[1]):
            for r2 in range(r + 1, matrix.shape[0] + 1):
                for c2 in range(c + 1, matrix.shape[1] + 1):
                    si = np.sum(matrix[r:r2, c:c2])
                    if si == -64:
                        sp = (r, c, r2 - 1, c2 - 1)
                        results.append(sp)
    if len(results) == 0:
        return []
    else:
        return results