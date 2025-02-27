import numpy as np

def submatrix_with_n_numbers(matrix):
    if np.issubdtype(matrix.dtype, np.integer):
        n = 138
        total = 0
        for r1 in range(matrix.shape[0]):
            for c1 in range(matrix.shape[1]):
                for r2 in range(r1, matrix.shape[0]):
                    for c2 in range(c1, matrix.shape[1]):
                        if len(matrix[r1:r2, c1:c2].flatten()) == n:
                            total += 1
        return total
    else:
        return 0