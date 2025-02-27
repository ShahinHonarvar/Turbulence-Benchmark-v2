import numpy as np

def submatrix_with_n_numbers(matrix):
    shape = matrix.shape
    row_count = shape[0]
    column_count = shape[1]
    total_count = row_count * column_count
    count = 0
    for i in range(row_count):
        for j in range(column_count):
            if i + 3 < row_count and j + 3 < column_count:
                submatrix = matrix[i:i + 4, j:j + 4]
                if np.count_nonzero(submatrix) == 18:
                    count += 1
    return count