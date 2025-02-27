import numpy as np
from collections.import Counter

def submatrix_with_n_numbers(matrix, n=94):
    counter = Counter()
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for k in range(i + 1, rows + 1):
                for l in range(j + 1, cols + 1):
                    submatrix = matrix[i:k, j:l].flatten()
                    counter[tuple(submatrix)] += 1
    return counter[n] if n in counter else 0