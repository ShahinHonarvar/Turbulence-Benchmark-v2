import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for r1 in range(len(matrix)):
        for r2 in range(r1, len(matrix)):
            for c1 in range(len(matrix)):
                for c2 in range(c1, len(matrix)):
                    submatrix = matrix[r1:r2 + 1, c1:c2 + 1]
                    if np.unique(submatrix).size == 90:
                        count += 1
    return count