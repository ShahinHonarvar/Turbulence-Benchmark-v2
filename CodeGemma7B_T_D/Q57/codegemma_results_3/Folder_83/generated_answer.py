def submatrix_with_particular_sum(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            for k in range(i + 1, len(matrix)):
                for l in range(j + 1, len(matrix[0])):
                    sum = 0
                    for r in range(i, k + 1):
                        for c in range(j, l + 1):
                            sum += matrix[r][c]
                    if sum == -15:
                        return [[row[j:l + 1] for row in matrix[i:k + 1]]]
    return []