def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if j + 60 <= len(matrix[0]):
                if matrix[i][j:j + 60].sum() == 60:
                    count += 1
    return count