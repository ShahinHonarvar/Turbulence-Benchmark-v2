def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix[k])):
                    if sum(matrix[i:k + 1][l:l + 1]) == 2:
                        submatrices.append((i, j, k, l))
    return submatrices