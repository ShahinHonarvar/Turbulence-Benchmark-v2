def submatrix_with_n_numbers(matrix):
    n = len(matrix)
    count = 0
    for i in range(n):
        for j in range(n):
            for k in range(i + 1, n):
                for l in range(j + 1, n):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if submatrix.size == 28:
                        count += 1
    return count