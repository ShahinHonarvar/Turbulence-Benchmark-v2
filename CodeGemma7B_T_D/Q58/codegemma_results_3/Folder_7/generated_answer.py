import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for row_start in range(len(matrix)):
        for row_end in range(row_start, len(matrix)):
            for col_start in range(len(matrix[0])):
                for col_end in range(col_start, len(matrix[0])):
                    submatrix = matrix[row_start:row_end + 1, col_start:col_end + 1]
                    if np.unique(submatrix).size == 1 and submatrix.size == 121:
                        count += 1
    return count