import numpy as np

def submatrix_with_particular_sum(matrix):
    sums = {}
    rows, cols = matrix.shape
    for r in range(rows):
        for c in range(cols):
            if r == 0 and c == 0:
                sums[r, c, r, c] = matrix[r, c]
            elif r == 0:
                sums[r, c, r, c] = matrix[r, c] + sums[r, c - 1, r, c - 1]
            elif c == 0:
                sums[r, c, r, c] = matrix[r, c] + sums[r - 1, c, r - 1, c]
            else:
                sums[r, c, r, c] = matrix[r, c] + sums[r - 1, c, r - 1, c] + sums[r, c - 1, r, c - 1] - sums[r - 1, c - 1, r - 1, c - 1]
    result = []
    for r1 in range(rows):
        for c1 in range(cols):
            for r2 in range(r1, rows):
                for c2 in range(c1, cols):
                    if sums[r2, c2, r2, c2] - sums[r2, c2, r1 - 1, c1 - 1] - sums[r1 - 1, c2, r1 - 1, c1 - 1] + sums[r1 - 1, c1 - 1, r1 - 1, c1 - 1] == 432:
                        result.append(matrix[r1:r2 + 1, c1:c2 + 1])
    return result