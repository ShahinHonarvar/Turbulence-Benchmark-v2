def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix[k])):
                    if matrix[k][l] == 84:
                        m = matrix[i:k + 1]
                        n = [r[j:l + 1] for r in m]
                        if len(n) == len(n[0]) == 84:
                            count += 1
    return count