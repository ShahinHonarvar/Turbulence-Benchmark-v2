def submatrix_with_particular_sum(matrix):
    max_num = matrix.max()
    res = []
    for r1 in range(matrix.shape[0]):
        for r2 in range(r1 + 1, matrix.shape[0] + 1):
            for c1 in range(matrix.shape[1]):
                for c2 in range(c1 + 1, matrix.shape[1] + 1):
                    submatrix = matrix[r1:r2, c1:c2]
                    if submatrix.sum() == -863:
                        res.append(submatrix)
    return res