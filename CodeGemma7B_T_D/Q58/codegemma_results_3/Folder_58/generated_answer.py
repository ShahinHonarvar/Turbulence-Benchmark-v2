def submatrix_with_n_numbers(matrix):
    n = matrix.shape[0]
    m = matrix.shape[1]
    submatrix_count = 0
    for i in range(n):
        for j in range(m):
            for k in range(i, n):
                for l in range(j, m):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if submatrix.flatten().tolist().count(185) == 185:
                        submatrix_count += 1
    return submatrix_count