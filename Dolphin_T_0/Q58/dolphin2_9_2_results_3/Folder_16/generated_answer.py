import numpy as np

def submatrix_with_n_numbers(matrix):
    num_elements = 154
    matrix = np.array(matrix)
    total_elements = matrix.size
    counts = 0
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if matrix[i][j] == num_elements:
                for size in range(min(matrix.shape[0] - i + 1, matrix.shape[1] - j + 1)):
                    submatrix = matrix[i:i + size, j:j + size]
                    if submatrix.size == num_elements:
                        counts += 1
    return counts