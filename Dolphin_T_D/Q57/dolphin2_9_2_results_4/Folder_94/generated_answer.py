def submatrix_with_particular_sum(matrix):
    m = len(matrix)
    n = len(matrix[0])
    submatrices = []
    for i in range(m):
        for j in range(n):
            for k in range(i, m):
                for l in range(j, n):
                    if sum((matrix[x][y] for x in range(i, k + 1) for y in range(j, l + 1))) == 92:
                        submatrices.append(matrix[i:k + 1, j:l + 1])
    return submatrices