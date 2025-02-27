def submatrix_with_n_numbers(matrix):
    count = 0
    for row1 in range(len(matrix)):
        for row2 in range(row1 + 1, len(matrix)):
            for col1 in range(len(matrix[0])):
                for col2 in range(col1 + 1, len(matrix[0])):
                    submatrix = [matrix[row][col] for row in range(row1, row2 + 1) for col in range(col1, col2 + 1)]
                    if len(set(submatrix)) == 2:
                        count += 1
    return count