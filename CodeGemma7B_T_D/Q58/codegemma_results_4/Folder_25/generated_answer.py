def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            for k in range(len(matrix[0])):
                count += matrix[i][k] < 66 and matrix[j][k] < 66 and (matrix[i][k] + matrix[j][k] + 66 == 198)
    return count