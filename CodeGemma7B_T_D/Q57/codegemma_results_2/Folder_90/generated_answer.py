def submatrix_with_particular_sum(matrix):
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            for k in range(len(matrix[0])):
                for l in range(k + 1, len(matrix[0])):
                    submatrix = [[matrix[i][k], matrix[i][l]], [matrix[j][k], matrix[j][l]]]
                    if sum([sum(row) for row in submatrix]) == -452:
                        return submatrix
    return []