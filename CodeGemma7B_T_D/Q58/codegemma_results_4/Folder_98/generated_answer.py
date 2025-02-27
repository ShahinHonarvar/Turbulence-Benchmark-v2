def submatrix_with_n_numbers(matrix):
    n = matrix.shape[0]
    count = 0
    for i in range(n):
        for j in range(n):
            for k in range(i + 1, n):
                for l in range(j + 1, n):
                    submatrix = matrix[i:k, j:l]
                    if submatrix.shape[0] * submatrix.shape[1] == 9 and all((num in submatrix for num in range(1, 10))):
                        count += 1
    return count