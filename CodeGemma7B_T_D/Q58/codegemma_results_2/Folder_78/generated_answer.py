import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for r1 in range(len(matrix)):
        for r2 in range(r1 + 1, len(matrix)):
            for c1 in range(len(matrix[0])):
                for c2 in range(c1 + 1, len(matrix[0])):
                    submatrix = matrix[r1:r2 + 1, c1:c2 + 1]
                    if np.count_nonzero(submatrix == 1) == 91:
                        count += 1
    return count