def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix[0])):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    submatrix_sum = submatrix.sum()
                    if submatrix_sum == -86:
                        submatrices.append(submatrix)
    return submatrices