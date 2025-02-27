def submatrix_with_particular_sum(matrix):
    res = []
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            for k in range(x, len(matrix)):
                for j in range(y, len(matrix[0])):
                    t = matrix[x][y]
                    if x > y:
                        for i in range(y + 1, x):
                            t += matrix[k][i]
                    elif x < y:
                        for i in range(x + 1, y):
                            t += matrix[k][i]
                    else:
                        t += matrix[k][j]
                    if matrix[k][j] + t == -255:
                        temp = [r[y:j + 1] for r in matrix[x:k + 1]]
                        res.append(temp)
    return res