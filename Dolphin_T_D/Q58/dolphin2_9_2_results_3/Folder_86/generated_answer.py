import numpy as np

def submatrix_with_n_numbers(matrix):
    n_rows, n_cols = matrix.shape
    count = 0
    for i in range(n_rows):
        for j in range(n_cols):
            if matrix[i, j] == 138:
                count_rows = 0
                for k in range(i, n_rows):
                    if all((matrix[k, j] == 138 for j in range(n_cols))):
                        count_rows += 1
                    else:
                        break
                    count_cols = 0
                    for l in range(j, n_cols):
                        if all((matrix[k, l] == 138 for k in range(i, i + count_rows))):
                            count_cols += 1
                        else:
                            break
                        if count_rows * count_cols == 138:
                            count += 1
    return count