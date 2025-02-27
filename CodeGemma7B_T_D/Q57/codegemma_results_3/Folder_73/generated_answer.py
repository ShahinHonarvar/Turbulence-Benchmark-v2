def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix[0])):
                    if sum((row[j:l + 1] for row in matrix[i:k + 1])) == 93:
                        submatrices.append([row[j:l + 1] for row in matrix[i:k + 1]])
    return submatrices