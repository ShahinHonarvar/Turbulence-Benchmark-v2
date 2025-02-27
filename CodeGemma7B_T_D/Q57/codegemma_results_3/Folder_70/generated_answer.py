def submatrix_with_particular_sum(matrix):
    for start_row in range(0, len(matrix)):
        for end_row in range(start_row, len(matrix)):
            for start_col in range(0, len(matrix[0])):
                for end_col in range(start_col, len(matrix[0])):
                    submatrix = matrix[start_row:end_row + 1, start_col:end_col + 1]
                    if submatrix.sum() == 411:
                        return [[row for row in submatrix]]
    return []