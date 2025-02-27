def submatrix_with_particular_sum(matrix):
    list_of_submatrices = []
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return list_of_submatrices
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix[0])):
                    if sum([row[j:l + 1] for row in matrix[i:k + 1]]) == -3:
                        list_of_submatrices.append(matrix[i:k + 1][j:l + 1])
    return list_of_submatrices