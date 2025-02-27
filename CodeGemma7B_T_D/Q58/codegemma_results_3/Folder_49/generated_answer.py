import numpy as np

def submatrix_with_n_numbers(arr):
    count = 0
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            for k in range(i, arr.shape[0]):
                for l in range(j, arr.shape[1]):
                    if np.sum(arr[i:k + 1, j:l + 1]) == 72:
                        count += 1
    return count