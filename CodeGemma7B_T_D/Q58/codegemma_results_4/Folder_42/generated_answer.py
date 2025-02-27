import numpy as np

def submatrix_with_n_numbers(matrix, num_numbers):
    count = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            submatrix = matrix[row:row + num_numbers, col:col + num_numbers]
            if np.all(np.isin(submatrix, [0, 193])):
                count += 1
    return count