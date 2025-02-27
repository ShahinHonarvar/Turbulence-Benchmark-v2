def submatrix_with_n_numbers(matrix):
    if len(matrix) == 0:
        return 0
    n = len(matrix[0])
    count = 0
    for start_row in range(len(matrix)):
        for end_row in range(start_row, len(matrix)):
            for start_col in range(n):
                for end_col in range(start_col, n):
                    submatrix = matrix[start_row:end_row + 1, start_col:end_col + 1]
                    if np.count_nonzero(submatrix == 21) == 21:
                        count += 1
    return count