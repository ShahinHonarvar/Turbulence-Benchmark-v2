import numpy as np
from itertools import product

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for start_row, end_row in product(range(rows), repeat=2):
        for start_col, end_col in product(range(cols), repeat=2):
            if (end_row - start_row + 1) * (end_col - start_col + 1) == 73:
                count += 1
    return count