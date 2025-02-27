import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    target_count = 138
    count = 0
    for r1 in range(rows):
        for r2 in range(r1 + 1, rows + 1):
            for c1 in range(cols):
                for c2 in range(c1 + 1, cols + 1):
                    submat = matrix[r1:r2, c1:c2]
                    if submat.size == target_count:
                        count += 1
    return count