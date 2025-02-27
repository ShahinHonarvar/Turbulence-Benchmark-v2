def submatrix_with_particular_sum(matrix):
    result = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == -42:
                result.append([[matrix[i][j]]])
    return result