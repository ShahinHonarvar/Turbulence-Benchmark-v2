import numpy as np
import itertools

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for row_start, row_end in itertools.product(range(rows), range(rows)):
        for col_start, col_end in itertools.product(range(cols), range(cols)):
            if row_end - row_start + 1 > 0 and col_end - col_start + 1 > 0 and ((row_end - row_start + 1) * (col_end - col_start + 1) == 21):
                submatrix = matrix[row_start:row_end + 1, col_start:col_end + 1]
                if submatrix.size == 21:
                    count += 1
    return count