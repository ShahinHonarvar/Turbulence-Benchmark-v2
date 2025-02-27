import numpy as np

def submatrix_with_particular_sum(matrix):
    above = np.cumsum(matrix, axis=0)
    left = np.cumsum(matrix.T, axis=0)
    res = set()
    for size in range(1, min(matrix.shape) + 1):
        for r1 in range(matrix.shape[0] - size + 1):
            for c1 in range(matrix.shape[1] - size + 1):
                r2, c2 = (r1 + size, c1 + size)
                total = above[r2 - 1, c2 - 1] - (left[r2 - 1, c1 - 1] if c1 - 1 >= 0 else 0) - (above[r1 - 1, c2 - 1] if r1 - 1 >= 0 else 0)
                if r1 > 0:
                    total += above[r1 - 1, c2 - 1]
                if c1 > 0:
                    total += left[r2 - 1, c1 - 1]
                if total == 99:
                    res.add((r1, c1, r2, c2))
    return [list(i) for i in res]