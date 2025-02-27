def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(i - 7, i + 1):
                for l in range(j - 7, j + 1):
                    if len({matrix[m][n] for m in range(k, i + 1) for n in range(l, j + 1)}) == 87:
                        count += 1
    return count