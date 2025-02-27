import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    n = 40
    for row in range(rows):
        for col in range(cols):
            submat_rows, submat_cols = (1, 1)
            while row + submat_rows <= rows and col + submat_cols <= cols:
                submat = matrix[row:row + submat_rows, col:col + submat_cols]
                if submat.size == n:
                    count += 1
                elif submat.size > n:
                    break
                submat_cols += 1
            submat_rows += 1
    return count