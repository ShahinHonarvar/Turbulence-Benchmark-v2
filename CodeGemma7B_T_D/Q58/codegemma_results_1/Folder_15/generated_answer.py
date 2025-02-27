def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            for k in range(j + 1, len(matrix)):
                for l in range(k + 1, len(matrix)):
                    if len(set(matrix[i][j:k + 1][l:k + 1])) == 2:
                        count += 1
    return count