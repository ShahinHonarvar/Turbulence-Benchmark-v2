import numpy as np

def submatrix_with_n_numbers(arr):
    low = np.min(arr) - 1
    high = np.max(arr) + 2
    result = 0
    for row in range(low, high):
        for col in range(low, high):
            for r in range(row, high):
                for c in range(col, high):
                    new_arr = arr[row:r + 1, col:c + 1]
                    if np.sum(new_arr) == 18:
                        result += 1
    return result