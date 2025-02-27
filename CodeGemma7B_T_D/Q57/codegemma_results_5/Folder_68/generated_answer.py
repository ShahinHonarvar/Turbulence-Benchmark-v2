def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix[k])):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if submatrix.sum() == 3:
                        submatrices.append(submatrix)
    return submatrices