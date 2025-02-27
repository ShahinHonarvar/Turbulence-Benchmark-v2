import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for h in range(i, matrix.shape[0]):
                for w in range(j, matrix.shape[1]):
                    if (h - i + 1) * (w - j + 1) == 191:
                        count += 1
    return count