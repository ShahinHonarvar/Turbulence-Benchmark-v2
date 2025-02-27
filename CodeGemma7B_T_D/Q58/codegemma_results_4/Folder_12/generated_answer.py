def submatrix_with_n_numbers(mat):
    rows, cols = mat.shape
    cnt = 0
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    submatrix = mat[i:k + 1, j:l + 1]
                    if submatrix.size == 46:
                        cnt += 1
    return cnt