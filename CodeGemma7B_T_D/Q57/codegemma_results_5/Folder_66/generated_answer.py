def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix)):
                    current_sum = 0
                    for m in range(i, k + 1):
                        for n in range(j, l + 1):
                            current_sum += matrix[m][n]
                    if current_sum == 99:
                        submatrices.append([matrix[x][y] for x in range(i, k + 1) for y in range(j, l + 1)])
    return submatrices