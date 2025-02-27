import numpy as np

def submatrix_with_n_numbers(matrix):
    n = matrix.shape
    total_count = 0
    for r1 in range(n[0]):
        for r2 in range(r1, n[0]):
            for c1 in range(n[1]):
                for c2 in range(c1, n[1]):
                    num_elements = (r2 - r1 + 1) * (c2 - c1 + 1)
                    if num_elements == 29:
                        total_count += 1
    return total_count