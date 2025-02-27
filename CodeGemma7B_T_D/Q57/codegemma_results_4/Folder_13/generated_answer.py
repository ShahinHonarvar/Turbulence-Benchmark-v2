def submatrix_with_particular_sum(matrix):
    if not matrix:
        return []
    submatrices = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix[0])):
                    submatrix = matrix[i:k + 1][j:l + 1]
                    if sum((sum(row) for row in submatrix)) == 382:
                        submatrices.append(submatrix)
    return submatrices