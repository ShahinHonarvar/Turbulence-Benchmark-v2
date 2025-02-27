import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for row1 in range(len(matrix)):
        for col1 in range(len(matrix[row1])):
            for row2 in range(row1, len(matrix)):
                for col2 in range(col1, len(matrix[row2])):
                    submatrix = matrix[row1:row2 + 1, col1:col2 + 1]
                    if np.count_nonzero(submatrix) == 96:
                        count += 1
    return count