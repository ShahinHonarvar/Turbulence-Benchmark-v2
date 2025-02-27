import numpy as np

def submatrix_with_n_numbers(matrix):
    submatrix_count = 0
    matrix_height, matrix_width = matrix.shape
    for height in range(matrix_height):
        for width in range(matrix_width):
            submatrix = matrix[height:, width:]
            submatrix_height, submatrix_width = submatrix.shape
            if submatrix_height < 2 or submatrix_width < 2:
                continue
            target = np.full((1, 1), 1)
            submatrix_count += sum((sum(submatrix[:h, :w] == target) for h in range(1, submatrix_height) for w in range(1, submatrix_width)))
    return submatrix_count