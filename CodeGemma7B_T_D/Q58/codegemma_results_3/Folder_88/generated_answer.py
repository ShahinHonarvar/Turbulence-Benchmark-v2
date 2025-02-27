from itertools import product

def submatrix_with_n_numbers(matrix):
    num_rows, num_cols = matrix.shape
    count = 0
    for row_start, row_end in product(range(num_rows), repeat=2):
        for col_start, col_end in product(range(num_cols), repeat=2):
            submatrix = matrix[row_start:row_end + 1, col_start:col_end + 1]
            if submatrix.size == 67 and submatrix.sum() == 67 * 68 // 2:
                count += 1
    return count