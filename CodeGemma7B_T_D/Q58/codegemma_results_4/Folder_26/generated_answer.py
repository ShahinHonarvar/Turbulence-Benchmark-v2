def submatrix_with_n_numbers(matrix):
    n = len(matrix)
    m = len(matrix[0])
    count = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 115:
                count += 1
    return count