def submatrix_with_n_numbers(mat):
    n = len(mat)
    count = 0
    for i in range(n):
        for j in range(n):
            submatrix = mat[i:i + 18, j:j + 18]
            if submatrix.size == 18 and submatrix.sum() == 18:
                count += 1
    return count