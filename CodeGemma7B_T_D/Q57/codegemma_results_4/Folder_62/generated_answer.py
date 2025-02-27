def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    submatrix_sum = matrix[i:k + 1, j:l + 1].sum()
                    if submatrix_sum == 394:
                        submatrices.append(matrix[i:k + 1, j:l + 1])
    return submatrices