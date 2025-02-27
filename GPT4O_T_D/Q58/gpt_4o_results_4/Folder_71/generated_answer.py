import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    target_count = 78
    count = 0
    for r1 in range(rows):
        for r2 in range(r1, rows):
            for c1 in range(cols):
                for c2 in range(c1, cols):
                    num_elements = (r2 - r1 + 1) * (c2 - c1 + 1)
                    if num_elements == target_count:
                        submatrix = matrix[r1:r2 + 1, c1:c2 + 1]
                        if submatrix.size == target_count:
                            count += 1
    return count