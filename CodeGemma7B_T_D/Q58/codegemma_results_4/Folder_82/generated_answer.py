def submatrix_with_n_numbers(matrix):
    count = 0
    for row1 in range(matrix.shape[0]):
        for row2 in range(row1, matrix.shape[0]):
            for col1 in range(matrix.shape[1]):
                for col2 in range(col1, matrix.shape[1]):
                    submatrix = matrix[row1:row2 + 1, col1:col2 + 1]
                    if np.count_nonzero(submatrix == 99) == 99:
                        count += 1
    return count