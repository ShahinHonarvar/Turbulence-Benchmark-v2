import numpy as np

def submatrix_with_n_numbers(arr):
    r, c = arr.shape
    count_matrices = 0
    for i in range(r - 1):
        for j in range(c - 1):
            count = 0
            for x in range(i, r):
                for y in range(j, c):
                    if arr[x][y] == 138:
                        count += 1
                    if count == 138:
                        count_matrices += 1
                        count = 0
    return count_matrices