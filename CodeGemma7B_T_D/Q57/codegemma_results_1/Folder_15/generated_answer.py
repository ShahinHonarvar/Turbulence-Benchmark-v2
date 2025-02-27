def submatrix_with_particular_sum(matrix):
    for x in range(len(matrix)):
        for y in range(len(matrix)):
            for a in range(x, len(matrix)):
                for b in range(y, len(matrix)):
                    for i in range(x, a + 1):
                        for j in range(y, b + 1):
                            if sum((matrix[i][j] for j in range(y, b + 1))) == -9 and sum((matrix[i][j] for i in range(x, a + 1))) == -9 and (sum((matrix[i][j] for i in range(x, a + 1))) == -9):
                                return [[matrix[i][j] for j in range(y, b + 1)] for i in range(x, a + 1)]
    return []