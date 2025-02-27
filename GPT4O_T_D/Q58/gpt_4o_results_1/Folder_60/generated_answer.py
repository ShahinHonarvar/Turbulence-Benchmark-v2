import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    n = 88
    submatrix_count = 0
    factors = [(i, n // i) for i in range(1, int(n ** 0.5) + 1) if n % i == 0]
    for r, c in factors:
        for i in range(rows - r + 1):
            for j in range(cols - c + 1):
                submatrix_count += 1
        if r != c:
            r, c = (c, r)
            for i in range(rows - r + 1):
                for j in range(cols - c + 1):
                    submatrix_count += 1
    return submatrix_count