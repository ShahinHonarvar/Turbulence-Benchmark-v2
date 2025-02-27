def submatrix_with_particular_sum(matrix):
    cols, rows = matrix.shape
    for i in range(rows):
        for j in range(i):
            for k in range(j, cols):
                for l in range(k, rows):
                    submatrix_sum = matrix[i:l + 1, j:k + 1].sum()
                    if submatrix_sum == -26:
                        return [[i, j], [l, k]]
    return []