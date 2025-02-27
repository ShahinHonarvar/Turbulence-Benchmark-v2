import numpy as np
from itertools import combinations

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for r in range(rows):
        for c in range(cols):
            for row_size in range(1, rows - r + 1):
                for col_size in range(1, cols - c + 1):
                    submatrix = matrix[r:r + row_size, c:c + col_size]
                    if submatrix.size == 21 and np.all(submatrix == submatrix.flatten()):
                        count += 1
    return count