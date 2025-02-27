def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(i + 1, len(matrix)):
                for l in range(j + 1, len(matrix[0])):
                    for m in range(i, k + 1):
                        for n in range(j, l + 1):
                            if np.all(matrix[m:k + 1, n:l + 1] == 85):
                                count += 1
    return count