import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    submatrix_size = 180
    submatrix_count = 0
    if submatrix_size > rows * cols:
        return 0
    total_elements = rows * cols
    submatrices_possible = total_elements // submatrix_size
    return submatrices_possible