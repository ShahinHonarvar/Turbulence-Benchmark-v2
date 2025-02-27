import numpy as np
from collections import Counter

def submatrix_with_n_numbers(matrix, n=35):
    count = 0
    rows, cols = matrix.shape
    for start_row in range(rows):
        for start_col in range(cols):
            for end_row in range(start_row + 1, rows + 1):
                for end_col in range(start_col + 1, cols + 1):
                    submatrix = matrix[start_row:end_row, start_col:end_col]
                    if Counter(submatrix.flatten())[35] == n:
                        count += 1
    return count