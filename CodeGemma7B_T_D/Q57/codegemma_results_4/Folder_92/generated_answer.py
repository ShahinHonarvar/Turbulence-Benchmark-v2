def submatrix_with_particular_sum(matrix):
    result = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for k in range(i + 1, matrix.shape[0]):
                for l in range(j + 1, matrix.shape[1]):
                    current_sum = sum((matrix[i][j] for i in range(i, k + 1) for j in range(j, l + 1)))
                    if current_sum == -3:
                        result.append([[matrix[r][c] for c in range(j, l + 1)] for r in range(i, k + 1)])
    return result