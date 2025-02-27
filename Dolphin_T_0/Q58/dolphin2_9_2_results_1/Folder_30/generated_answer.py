import numpy as np

def submatrix_with_n_numbers(matrix):
    total = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for x in range(i + 1, len(matrix)):
                for y in range(j + 1, len(matrix[0])):
                    if np.count_nonzero(matrix[i:x, j:y]) == 94:
                        total += 1
    return total