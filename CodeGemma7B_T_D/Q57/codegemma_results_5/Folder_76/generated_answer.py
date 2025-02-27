def submatrix_with_particular_sum(matrix):
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix) + 1):
            for k in range(len(matrix[0])):
                for l in range(k + 1, len(matrix[0]) + 1):
                    submatrix = matrix[i:j, k:l]
                    if submatrix.sum() == -255:
                        return list(submatrix)
    return []