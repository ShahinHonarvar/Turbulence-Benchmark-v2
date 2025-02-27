def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            for m in range(len(matrix[0])):
                for n in range(m + 1, len(matrix[0])):
                    if len({matrix[i][m], matrix[i][n], matrix[j][m], matrix[j][n]}) == 4:
                        count += 1
    return count