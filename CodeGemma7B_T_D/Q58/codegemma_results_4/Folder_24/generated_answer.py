import numpy as np

def submatrix_with_n_numbers(arr):
    """
    Count submatrix of size n*n in a matrix contain n number
    """
    n = 51
    count = 0
    for r1 in range(len(arr)):
        for r2 in range(r1, len(arr)):
            for c1 in range(len(arr[0])):
                for c2 in range(c1, len(arr[0])):
                    matrix = arr[r1:r2 + 1, c1:c2 + 1]
                    if len(matrix) == n and len(matrix[0]) == n:
                        if np.all(matrix == 1):
                            count += 1
    return count