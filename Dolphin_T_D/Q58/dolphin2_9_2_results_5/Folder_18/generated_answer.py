def submatrix_with_n_numbers(mat):
    num_rows, num_cols = mat.shape
    submatrices_count = 0
    for i in range(num_rows - 2):
        for j in range(num_cols - 2):
            if mat[i][j] + mat[i + 1][j] + mat[i][j + 1] + mat[i + 1][j + 1] + mat[i][j - 1] + mat[i - 1][j] + mat[i - 1][j - 1] + mat[i - 1][j + 1] == 104:
                submatrices_count += 1
    return submatrices_count