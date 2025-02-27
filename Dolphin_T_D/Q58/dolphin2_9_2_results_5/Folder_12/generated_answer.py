import numpy as np

def submatrix_with_n_numbers(matrix):
    shape = matrix.shape
    filter_width = 46
    if shape[0] * shape[1] != filter_width * filter_width:
        return 0
    return shape[0] * shape[1] // filter_width