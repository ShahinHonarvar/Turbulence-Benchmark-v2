def submatrix_with_particular_sum(matrix):
    r, c = matrix.shape
    for i in range(r):
        for j in range(c):
            for k in range(i, r):
                for l in range(j, c):
                    sum = 0
                    for m in range(i, k + 1):
                        for n in range(j, l + 1):
                            sum += matrix[m][n]
                    if sum == 69:
                        return [[matrix[i][j:l + 1] for j in range(c) if j in range(i, k + 1)] for i in range(r) if i in range(j, k + 1)]
    return []