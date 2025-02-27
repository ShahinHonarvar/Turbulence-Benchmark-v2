def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            for k in range(len(matrix[0])):
                for l in range(k + 1, len(matrix[0])):
                    if sum(matrix[i][k:l + 1]) == sum(matrix[j][k:l + 1]) and matrix[i][k:l + 1] == matrix[j][k:l + 1]:
                        count += 1
    return count