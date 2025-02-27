import numpy as np

def submatrix_with_n_numbers(matrix):
    n_elements = 68
    num_rows, num_cols = matrix.shape
    count = 0
    for i in range(num_rows):
        for j in range(num_cols):
            if matrix[i][j] == 1:
                for x in range(i, num_rows):
                    for y in range(j, num_cols):
                        if (x - i + 1) * (y - j + 1) == n_elements:
                            submatrix = matrix[i:x + 1, j:y + 1]
                            count += 1
    return count