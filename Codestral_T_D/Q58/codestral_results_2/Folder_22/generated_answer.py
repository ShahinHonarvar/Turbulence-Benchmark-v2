import numpy as np
from collections import Counter

def submatrix_with_n_numbers(matrix, n=21):
    rows, cols = matrix.shape
    submatrix_count = 0
    for i in range(rows - 3):
        for j in range(cols - 3):
            submatrix = matrix[i:i + 4, j:j + 4].flatten()
            if Counter(submatrix) == Counter({21: n}):
                submatrix_count += 1
    return submatrix_count