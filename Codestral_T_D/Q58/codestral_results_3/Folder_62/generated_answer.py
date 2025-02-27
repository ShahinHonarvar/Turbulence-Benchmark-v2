import numpy as np

def submatrix_with_n_numbers(matrix, n=186):
    r, c = matrix.shape
    count = 0
    for x in range(r):
        for y in range(c):
            for i in range(x, r):
                for j in range(y, c):
                    if np.sum(matrix[x:i + 1, y:j + 1]) == n:
                        count += 1
    return count