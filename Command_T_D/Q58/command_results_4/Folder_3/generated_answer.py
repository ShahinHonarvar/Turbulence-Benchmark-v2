import numpy as np

def submatrix_with_n_numbers(arr):
    row = arr.shape[0]
    col = arr.shape[1]
    if row < col:
        return 0
    else:
        return np.sum(np.sum(arr[0:row - 1], axis=0) == row - 1)