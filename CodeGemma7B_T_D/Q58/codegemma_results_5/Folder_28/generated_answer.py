def submatrix_with_n_numbers(matrix):
    count = 0
    for m in range(len(matrix)):
        for n in range(len(matrix[0])):
            for k in range(m, len(matrix)):
                for l in range(n, len(matrix[0])):
                    submatrix = matrix[m:k + 1][:, n:l + 1]
                    if (submatrix == 37).sum() == 37:
                        count += 1
    return count