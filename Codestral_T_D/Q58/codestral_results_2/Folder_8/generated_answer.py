import numpy as np
from collections import Counter

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 1):
        for j in range(cols - 1):
            for k in range(i + 2, rows + 1):
                for l in range(j + 2, cols + 1):
                    submatrix = matrix[i:k, j:l]
                    if Counter(submatrix.flatten())[29] == (k - i) * (l - j):
                        count += 1
    return count