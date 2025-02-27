import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i, j] == 154:
                if np.count_nonzero(matrix[i:i + 6, j:j + 6]) == 154:
                    count += 1
    return count