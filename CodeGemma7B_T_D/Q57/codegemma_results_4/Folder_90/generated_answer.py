def submatrix_with_particular_sum(matrix):
    result = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            for k in range(i + 1):
                for l in range(j + 1):
                    submatrix = matrix[k:i + 1, l:j + 1]
                    if submatrix.sum() == -452:
                        result.append(submatrix)
    return result