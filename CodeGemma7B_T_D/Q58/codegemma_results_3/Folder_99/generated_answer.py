def submatrix_with_n_numbers(matrix):
    count = 0
    for row1 in range(len(matrix)):
        for row2 in range(row1, len(matrix)):
            for col1 in range(len(matrix[0])):
                for col2 in range(col1, len(matrix[0])):
                    submatrix = matrix[row1:row2 + 1, col1:col2 + 1]
                    if np.count_nonzero(submatrix) == 146:
                        count += 1
    return count