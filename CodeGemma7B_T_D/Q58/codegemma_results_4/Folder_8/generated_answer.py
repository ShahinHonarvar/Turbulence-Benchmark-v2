def submatrix_with_n_numbers(matrix):
    row_count = len(matrix)
    col_count = len(matrix[0])
    count = 0
    for row1 in range(row_count):
        for row2 in range(row1, row_count):
            for col1 in range(col_count):
                for col2 in range(col1, col_count):
                    submatrix = matrix[row1:row2 + 1][col1:col2 + 1]
                    if len(submatrix) == 29:
                        count += 1
    return count