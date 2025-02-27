import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    target_count = 27
    for r1 in range(rows):
        for r2 in range(r1 + 1, rows + 1):
            for c1 in range(cols):
                for c2 in range(c1 + 1, cols + 1):
                    submatrix_elements_count = (r2 - r1) * (c2 - c1)
                    if submatrix_elements_count == target_count:
                        count += 1
    return count