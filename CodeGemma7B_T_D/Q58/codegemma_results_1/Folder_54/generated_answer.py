from itertools import combinations_with_replacement as cwr

def submatrix_with_n_numbers(matrix):
    ROWS, COLS = matrix.shape
    count = 0
    for row1, row2 in cwr(range(ROWS), 2):
        for col1, col2 in cwr(range(COLS), 2):
            if row1 <= row2 and col1 <= col2:
                submatrix = matrix[row1:row2 + 1, col1:col2 + 1]
                if submatrix.size == 27 and submatrix.sum() == 27 * 26 // 2:
                    count += 1
    return count