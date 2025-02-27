import numpy as np

def submatrix_with_particular_sum(arr):
    mask = np.sum(arr, axis=1) == -47
    return np.where(mask)[0]