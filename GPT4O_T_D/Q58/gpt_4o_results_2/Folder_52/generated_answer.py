import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    row_count = matrix.shape[0]
    col_count = matrix.shape[1]
    n = 147
    max_size = int(np.sqrt(n))
    for size in range(1, max_size + 1):
        if n % size == 0:
            sub_rows, sub_cols = (size, n // size)
            if sub_rows <= row_count and sub_cols <= col_count:
                for i in range(row_count - sub_rows + 1):
                    for j in range(col_count - sub_cols + 1):
                        submatrix = matrix[i:i + sub_rows, j:j + sub_cols]
                        if submatrix.size == n:
                            count += 1
            if sub_cols <= row_count and sub_rows <= col_count and (sub_rows != sub_cols):
                for i in range(row_count - sub_cols + 1):
                    for j in range(col_count - sub_rows + 1):
                        submatrix = matrix[i:i + sub_cols, j:j + sub_rows]
                        if submatrix.size == n:
                            count += 1
    return count