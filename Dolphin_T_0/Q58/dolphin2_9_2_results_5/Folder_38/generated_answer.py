import numpy as np

def submatrix_with_n_numbers(matrix):
    size = matrix.size
    if size % 34 != 0 or size < 34:
        return 0
    else:
        combinations = np.combin(matrix, 34)
        return combinations.size