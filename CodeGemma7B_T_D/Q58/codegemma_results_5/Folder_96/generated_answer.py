def submatrix_with_n_numbers(matrix):
    n = 20
    cnt = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] > 20:
                continue
            tmp = [0 for _ in range(20)]
            length = 0
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix[0])):
                    tmp[matrix[k][l]] += 1
                    length += 1
                    if length == n:
                        cnt += 1
                    elif length > n:
                        break
            tmp = [t for t in tmp if t > 0]
            for p in tmp:
                if p == n:
                    cnt += 1
    return cnt