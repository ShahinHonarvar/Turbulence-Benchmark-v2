def submatrix_with_n_numbers(matrix):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return 0
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 74:
                for k in range(i, len(matrix)):
                    for l in range(j, len(matrix[0])):
                        if len({matrix[r][c] for r in range(i, k + 1) for c in range(j, l + 1)}) == 74:
                            count += 1
    return count