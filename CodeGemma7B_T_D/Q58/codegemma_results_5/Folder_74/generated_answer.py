def submatrix_with_n_numbers(matrix):
    n = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            for k in range(i + 1, len(matrix)):
                for l in range(j + 1, len(matrix)):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if len(submatrix) == 48:
                        n += 1
    return n