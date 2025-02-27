def submatrix_with_particular_sum(matrix):
    submatrices = []
    for row in range(matrix.shape[0]):
        for col in range(matrix.shape[1]):
            for row2 in range(row, matrix.shape[0]):
                for col2 in range(col, matrix.shape[1]):
                    submatrix = matrix[row:row2 + 1, col:col2 + 1]
                    if submatrix.sum() == 126:
                        submatrices.append(submatrix)
    return submatrices