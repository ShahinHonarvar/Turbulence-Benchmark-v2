def submatrix_with_n_numbers(matrix):
    sum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 7:
                sum += 1
    return sum