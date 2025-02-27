import numpy as np
from itertools import combinations

def submatrix_with_n_numbers(matrix, n=57):
    rows, cols = matrix.shape
    count = 0
    for r in range(rows):
        for c in range(cols):
            for rs in range(r, rows):
                for cs in range(c, cols):
                    submatrix = matrix[r:rs + 1, c:cs + 1]
                    if submatrix.size == n and np.all(submatrix == 57):
                        count += 1
    return count