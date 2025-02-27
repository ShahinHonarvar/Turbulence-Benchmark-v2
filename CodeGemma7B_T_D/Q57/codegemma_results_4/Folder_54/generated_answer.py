def submatrix_with_particular_sum(matrix):
    result = []
    for i in range(matrix.shape[0]):
        for j in range(i, matrix.shape[0]):
            for k in range(matrix.shape[1]):
                for l in range(k, matrix.shape[1]):
                    submatrix = matrix[i:j + 1, k:l + 1]
                    if submatrix.sum() == -59:
                        result.append(submatrix)
    return result