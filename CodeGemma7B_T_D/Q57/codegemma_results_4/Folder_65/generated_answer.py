def submatrix_with_particular_sum(matrix):
    submatrices = []
    for row1 in range(len(matrix)):
        for row2 in range(row1, len(matrix)):
            for col1 in range(len(matrix[0])):
                for col2 in range(col1, len(matrix[0])):
                    submatrix = matrix[row1:row2 + 1, col1:col2 + 1]
                    if sum(sum(submatrix)) == 78:
                        submatrices.append(submatrix)
    return submatrices