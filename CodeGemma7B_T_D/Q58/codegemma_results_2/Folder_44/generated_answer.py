def submatrix_with_n_numbers(matrix):
    submatrix_count = 0
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    sub_matrix = matrix[i:k + 1, j:l + 1]
                    if sub_matrix.shape[0] * sub_matrix.shape[1] == 191:
                        submatrix_count += 1
    return submatrix_count