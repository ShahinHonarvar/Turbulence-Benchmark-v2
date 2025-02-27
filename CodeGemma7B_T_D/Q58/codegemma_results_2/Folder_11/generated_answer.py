def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(len(matrix) - i):
                for l in range(len(matrix[0]) - j):
                    submatrix = matrix[i:i + k + 1, j:j + l + 1]
                    if submatrix.sum() == 38 * (k + 1) * (l + 1):
                        count += 1
    return count