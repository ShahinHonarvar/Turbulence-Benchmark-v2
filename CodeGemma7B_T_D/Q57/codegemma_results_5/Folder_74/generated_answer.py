def submatrix_with_particular_sum(mat):
    res = []
    for i in range(len(mat)):
        for j in range(i + 1, len(mat)):
            for k in range(len(mat[0])):
                for l in range(k + 1, len(mat[0])):
                    s = 0
                    for r in range(i, j + 1):
                        for c in range(k, l + 1):
                            s += mat[r][c]
                    if s == 88:
                        tmp = []
                        for r in range(i, j + 1):
                            tmp.append(mat[r][k:l + 1])
                        res.append(tmp)
    return res