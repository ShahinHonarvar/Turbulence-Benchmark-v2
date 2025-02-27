def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            for k in range(len(matrix[i])):
                for l in range(k, len(matrix[i])):
                    submatrix = matrix[i:j + 1, k:l + 1]
                    if len(np.unique(submatrix.flatten())) == 34:
                        count += 1
    return count