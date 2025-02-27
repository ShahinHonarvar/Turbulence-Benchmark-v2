def submatrix_with_n_numbers(num_matrix):
    matrix_size = len(num_matrix)
    count = 0
    for row1 in range(matrix_size):
        for row2 in range(row1, matrix_size):
            col_seen = set()
            for col in range(matrix_size):
                num = num_matrix[row1][col]
                if num in col_seen:
                    break
                col_seen.add(num)
            if len(col_seen) == 21:
                for r in range(row1, row2 + 1):
                    count += 1
    return count