import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, columns = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(columns):
            if (rows - i) * (columns - j) >= 138:
                submatrix_sum = np.sum(matrix[i:, j:])
                if submatrix_sum == 138:
                    count += 1
    return count