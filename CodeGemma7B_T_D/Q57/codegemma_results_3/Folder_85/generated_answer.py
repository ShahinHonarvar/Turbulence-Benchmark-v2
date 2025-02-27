def submatrix_with_particular_sum(matrix):
    result = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix[0])):
                    sum = 0
                    for m in range(i, k + 1):
                        for n in range(j, l + 1):
                            sum += matrix[m][n]
                    if sum == -87:
                        result.append([[matrix[r][s] for s in range(j, l + 1)] for r in range(i, k + 1)])
    return result