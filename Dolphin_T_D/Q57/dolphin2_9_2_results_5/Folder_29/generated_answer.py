import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    sums = {}
    for r in range(rows):
        for c in range(cols):
            if r == 0 and c == 0:
                pass
            elif r == 0:
                sums[r, c] = matrix[r, c] + sums[r, c - 1]
            elif c == 0:
                sums[r, c] = matrix[r, c] + sums[r - 1, c]
            else:
                sums[r, c] = matrix[r, c] + sums[r - 1, c] + sums[r, c - 1] - sums[r - 1, c - 1]
    results = []
    for r1 in range(rows):
        for c1 in range(cols):
            for r2 in range(r1, rows):
                for c2 in range(c1, cols):
                    submatrix_sum = sums[r2, c2] - (sums[r2, c1 - 1] if c1 > 0 else 0) - (sums[r1 - 1, c2] if r1 > 0 else 0) + (sums[r1 - 1, c1 - 1] if r1 > 0 and c1 > 0 else 0)
                    if submatrix_sum == 84:
                        submatrix = matrix[r1:r2 + 1, c1:c2 + 1]
                        results.append(submatrix)
    return results