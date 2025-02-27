import numpy as np

def submatrix_with_n_numbers(matrix):
    matrix = np.array(matrix)
    rows, cols = matrix.shape
    count = 0
    submatrix_size = 88
    submatrix_dimension = int(np.sqrt(submatrix_size))
    if submatrix_dimension * submatrix_dimension != submatrix_size:
        return 0
    for i in range(rows - submatrix_dimension + 1):
        for j in range(cols - submatrix_dimension + 1):
            if matrix[i:i + submatrix_dimension, j:j + submatrix_dimension].size == submatrix_size:
                count += 1
    return count