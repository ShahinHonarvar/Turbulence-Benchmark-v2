import numpy as np

def submatrix_with_n_numbers(matrix):
    n, m = matrix.shape
    if n * m < 180:
        return 0
    count = 0
    for r in range(n):
        for c in range(m):
            for height in range(1, n - r + 1):
                width = 180 // height
                if c + width <= m and width * height == 180:
                    count += 1
    return count