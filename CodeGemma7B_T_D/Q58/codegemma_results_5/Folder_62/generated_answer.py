import numpy as np

def submatrix_with_n_numbers(matrix):
    c = 0
    for r in range(matrix.shape[0]):
        for c in range(matrix.shape[1]):
            for r1 in range(r, matrix.shape[0]):
                for c1 in range(c, matrix.shape[1]):
                    if (r1 - r + 1) * (c1 - c + 1) == 186:
                        temp = matrix[r:r1 + 1, c:c1 + 1].flatten().sum()
                        if temp == 186:
                            c += 1
    if c == 0:
        return 0
    else:
        return c