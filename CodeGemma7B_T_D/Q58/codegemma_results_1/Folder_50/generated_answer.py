def submatrix_with_n_numbers(matrix):
    count = 0
    M, N = matrix.shape
    for i in range(M):
        for j in range(N):
            for r in range(i + 1, M):
                for c in range(j + 1, N):
                    if (matrix[i:r + 1, j:c + 1] == 40).sum() == 40:
                        count += 1
    return count