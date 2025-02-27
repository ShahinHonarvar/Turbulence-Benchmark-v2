def submatrix_with_particular_sum(matrix):
    ans = []
    for h in range(matrix.shape[0]):
        for k in range(h, matrix.shape[0]):
            for l in range(matrix.shape[1]):
                for r in range(l, matrix.shape[1]):
                    submatrix = matrix[h:k + 1, l:r + 1]
                    if submatrix.sum() == 398:
                        ans.append(submatrix)
    return ans