import numpy as np

def submatrix_with_n_numbers(matrix):
    result = 0
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            for r1 in range(r, len(matrix)):
                for c1 in range(c, len(matrix[r])):
                    temp = matrix[r:r1 + 1, c:c1 + 1]
                    if np.count_nonzero(temp == 57) == 57:
                        result += 1
    return result