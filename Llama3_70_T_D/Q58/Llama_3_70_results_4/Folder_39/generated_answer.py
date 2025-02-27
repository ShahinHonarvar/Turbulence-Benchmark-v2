import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for row in range(rows):
        for col in range(cols):
            for r_offset in range(rows - row + 1):
                for c_offset in range(cols - col + 1):
                    submatrix = matrix[row:row + r_offset, col:col + c_offset]
                    if np.prod(submatrix.shape) == 59:
                        count += 1
    return count