import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    if rows * cols < 88:
        return 0
    total_count = 0
    for sr in range(rows):
        for sc in range(cols):
            for er in range(sr, rows):
                for ec in range(sc, cols):
                    if (er - sr + 1) * (ec - sc + 1) == 88:
                        total_count += 1
    return total_count