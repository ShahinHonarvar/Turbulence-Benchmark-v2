import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    target_count = 122
    count = 0
    for top in range(rows):
        for left in range(cols):
            for bottom in range(top, rows):
                for right in range(left, cols):
                    submatrix = matrix[top:bottom + 1, left:right + 1]
                    if submatrix.size == target_count:
                        count += 1
    return count