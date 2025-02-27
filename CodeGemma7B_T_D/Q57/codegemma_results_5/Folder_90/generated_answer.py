def submatrix_with_particular_sum(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix)):
                    sum = 0
                    for m in range(i, k + 1):
                        for n in range(j, l + 1):
                            sum += matrix[m][n]
                    if sum == -452:
                        return [[matrix[m][n] for n in range(j, l + 1)] for m in range(i, k + 1)]
    return []