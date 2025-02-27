import numpy as np

def submatrix_with_n_numbers(matrix):
    matrix = np.array(matrix)
    n = 87
    count = 0
    for row in range(matrix.shape[0]):
        for col in range(matrix.shape[1]):
            for length1 in range(1, min(matrix.shape[0] - row, matrix.shape[1] - col) + 1):
                for length2 in range(1, min(matrix.shape[0] - row, matrix.shape[1] - col, length1) + 1):
                    submatrix = matrix[row:row + length1, col:col + length2]
                    if len(submatrix) == n:
                        count += 1
    return count