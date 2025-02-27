def submatrix_with_particular_sum(matrix):
    for x in range(len(matrix)):
        for y in range(len(matrix)):
            for a in range(x, len(matrix)):
                for b in range(y, len(matrix)):
                    summ = 0
                    for i in range(x, a + 1):
                        for j in range(y, b + 1):
                            summ += matrix[i][j]
                    if summ == 901:
                        return [[matrix[m][n] for n in range(y, b + 1)] for m in range(x, a + 1)]
    return []