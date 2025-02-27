import numpy as np
from itertools import combinations

def submatrix_with_n_numbers(matrix, n=34):
    if matrix.size < n:
        return 0
    count = 0
    rows, cols = matrix.shape
    for r in range(1, rows + 1):
        for c in range(1, cols + 1):
            for r_start in range(rows - r + 1):
                for c_start in range(cols - c + 1):
                    submatrix = matrix[r_start:r_start + r, c_start:c_start + c]
                    if np.count_nonzero(submatrix == 34) == n:
                        count += 1
    return count