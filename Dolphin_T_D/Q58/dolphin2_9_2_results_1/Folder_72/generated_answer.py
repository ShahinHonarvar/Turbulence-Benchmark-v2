import numpy as np

def submatrix_with_n_numbers(matrix):
    row_range, col_range = matrix.shape
    count = 0
    for i in range(row_range):
        for j in range(col_range):
            for k in range(i, row_range):
                for l in range(j, col_range):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if len(submatrix) == 4 and len(submatrix[0]) == 4:
                        count += 1
    if count > 0:
        return count
    else:
        return 0