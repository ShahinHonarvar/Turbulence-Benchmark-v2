def submatrix_with_particular_sum(matrix):
    result = []
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix) + 1):
            for k in range(len(matrix)):
                for l in range(k + 1, len(matrix) + 1):
                    submatrix = matrix[i:j, k:l]
                    if submatrix.sum() == -86:
                        result.append(submatrix)
    return result