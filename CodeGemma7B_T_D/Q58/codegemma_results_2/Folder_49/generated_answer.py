def submatrix_with_n_numbers(matrix):
    count = 0
    for r in range(len(matrix)):
        for i in range(r + 1, len(matrix) + 1):
            for j in range(len(matrix[0])):
                for k in range(j + 1, len(matrix[0]) + 1):
                    submatrix = matrix[r:i, j:k]
                    if np.count_nonzero(submatrix) == 72:
                        count += 1
    return count