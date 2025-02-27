def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                for k in range(i, len(matrix)):
                    for l in range(j, len(matrix[0])):
                        if sum((row[j:l + 1] for row in matrix[i:k + 1])) == 1:
                            count += 1
    return count