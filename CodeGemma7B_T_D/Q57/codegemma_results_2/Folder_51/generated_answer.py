def submatrix_with_particular_sum(matrix):
    submatrices = []
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(i, rows):
            for k in range(cols):
                for l in range(k, cols):
                    submatrix = matrix[i:j + 1, k:l + 1]
                    submatrix_sum = submatrix.sum()
                    if submatrix_sum == -46:
                        submatrices.append(submatrix)
    return submatrices