import numpy as np

def submatrix_with_n_numbers(matrix):
    n = matrix.size
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if len(np.where(matrix[i:i + len(matrix), j:j + len(matrix[0])] == 1)[0]) == 1:
                count += 1
    return count