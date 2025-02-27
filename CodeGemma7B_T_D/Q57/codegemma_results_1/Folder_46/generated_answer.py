def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            for k in range(j + 1, len(matrix)):
                for l in range(k + 1, len(matrix)):
                    submatrix = matrix[i:j + 1, k:l + 1]
                    if submatrix.sum() == 416:
                        submatrices.append(submatrix)
    return submatrices