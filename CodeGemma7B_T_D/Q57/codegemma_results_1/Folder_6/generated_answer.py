def submatrix_with_particular_sum(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix)):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if submatrix.sum() == 126:
                        return [submatrix]
    return []