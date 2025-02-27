def submatrix_with_particular_sum(matrix):
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            for k in range(len(matrix)):
                for l in range(k, len(matrix)):
                    if sum(matrix[i:j + 1][k:l + 1]) == -86:
                        return [[row[k:l + 1] for row in matrix[i:j + 1]]]
    return []