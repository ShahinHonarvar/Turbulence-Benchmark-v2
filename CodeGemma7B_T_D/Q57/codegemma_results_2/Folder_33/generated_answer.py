def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    cum_sums = np.cumsum(matrix, axis=0)
    res = []
    for i in range(rows):
        for j in range(i + 1, rows):
            for k in range(cols):
                for l in range(k + 1, cols):
                    sum_submatrix = cum_sums[j][l] - cum_sums[j][k] - cum_sums[i][l] + cum_sums[i][k]
                    if sum_submatrix == -811:
                        submatrix = matrix[i:j + 1, k:l + 1]
                        res.append(submatrix.tolist())
    return res