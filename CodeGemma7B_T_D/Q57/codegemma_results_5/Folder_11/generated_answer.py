def submatrix_with_particular_sum(matrix):
    res = []
    for row1 in range(len(matrix)):
        for row2 in range(row1, len(matrix)):
            for col1 in range(len(matrix[0])):
                for col2 in range(col1, len(matrix[0])):
                    if sum((row[col1:col2 + 1] for row in matrix[row1:row2 + 1])) == 38:
                        res.append([row[col1:col2 + 1] for row in matrix[row1:row2 + 1]])
    return res