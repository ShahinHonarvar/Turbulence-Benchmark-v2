def submatrix_with_particular_sum(matrix):
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            for k in range(len(matrix)):
                for l in range(k + 1, len(matrix)):
                    sum = 0
                    for m in range(i, j + 1):
                        for n in range(k, l + 1):
                            sum += matrix[m][n]
                    if sum == -936:
                        temp = [[x for x in row[k:l + 1]] for row in matrix[i:j + 1]]
                        result.append(temp)
    if not result:
        return []
    return result