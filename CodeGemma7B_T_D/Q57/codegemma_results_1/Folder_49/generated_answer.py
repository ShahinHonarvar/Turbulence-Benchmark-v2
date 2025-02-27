def submatrix_with_particular_sum(matrix):
    result = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for m in range(i, len(matrix)):
                for n in range(j, len(matrix[0])):
                    submatrix = matrix[i:m + 1, j:n + 1]
                    if submatrix.sum() == -42:
                        result.append(submatrix)
    return result