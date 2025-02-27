def submatrix_with_n_numbers(matrix):
    row_count = len(matrix)
    col_count = len(matrix[0])
    count = 0
    for i in range(row_count):
        for j in range(col_count):
            for k in range(i, row_count):
                for l in range(j, col_count):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if len(submatrix) * len(submatrix[0]) == 186:
                        count += 1
    return count