def submatrix_with_particular_sum(matrix):
    result = []
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            for k in range(len(matrix)):
                for l in range(k + 1, len(matrix)):
                    submatrix = matrix[i:j + 1, k:l + 1]
                    sum_of_submatrix = submatrix.sum()
                    if sum_of_submatrix == 92:
                        result.append(submatrix)
    return result