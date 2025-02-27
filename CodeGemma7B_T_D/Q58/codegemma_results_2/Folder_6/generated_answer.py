def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            for m in range(i + 1, len(matrix)):
                for n in range(j + 1, len(matrix)):
                    submatrix = matrix[i:m + 1, j:n + 1]
                    if len(submatrix) == 122:
                        count += 1
    return count