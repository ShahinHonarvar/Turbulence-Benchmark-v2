def submatrix_with_particular_sum(matrix):
    size = matrix.shape[0]
    list_of_submatrix = []
    for i in range(size):
        for j in range(size):
            for k in range(i, size):
                for l in range(j, size):
                    sum = 0
                    for m in range(i, k + 1):
                        for n in range(j, l + 1):
                            sum += matrix[m, n]
                    if sum == -47:
                        for m in range(i, k + 1):
                            for n in range(j, l + 1):
                                list_of_submatrix.append(matrix[m, n])
    return list_of_submatrix