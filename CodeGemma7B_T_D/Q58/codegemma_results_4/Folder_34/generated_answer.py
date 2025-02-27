def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            for k in range(len(matrix[0])):
                for l in range(k + 1, len(matrix[0])):
                    if all((matrix[i][k] in matrix[row][k] for row in range(i, j + 1))) and all((matrix[i][k] in matrix[i][col] for col in range(k, l + 1))):
                        count += 1
    return count