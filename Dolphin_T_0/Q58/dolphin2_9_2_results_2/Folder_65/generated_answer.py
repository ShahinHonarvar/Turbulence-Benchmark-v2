import numpy as np
from scipy.ndimage import sliding_window

def submatrix_with_n_numbers(matrix):
    counter = 0
    submatrices = sliding_window(matrix, (2, 2))
    for submatrix in submatrices:
        if np.count_nonzero(submatrix) == 35:
            counter += 1
    return counter if counter > 0 else 0