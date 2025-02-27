def submatrix_with_particular_sum(matrix):
    result = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix[0])):
                    current_sum = 0
                    for m in range(i, k + 1):
                        for n in range(j, l + 1):
                            current_sum += matrix[m][n]
                    if current_sum == 34:
                        result.append([[matrix[m][n] for n in range(j, l + 1)] for m in range(i, k + 1)])
    return result