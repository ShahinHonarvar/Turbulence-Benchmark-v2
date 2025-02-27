def submatrix_with_particular_sum(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows):
        for j in range(i, rows):
            for k in range(cols):
                for l in range(k, cols):
                    submatrix = matrix[i:j + 1][k:l + 1]
                    if sum((sum(row) for row in submatrix)) == 93:
                        return [submatrix]
    return []