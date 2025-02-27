import numpy as np
from collections import Counter

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    h, w = matrix.shape
    count = 0
    for i in range(h):
        for j in range(w):
            for x in range(i, h):
                for y in range(j, w):
                    submatrix = matrix[i:x + 1, j:y + 1]
                    if Counter(submatrix.flatten())[107] == submatrix.size:
                        count += 1
    return count