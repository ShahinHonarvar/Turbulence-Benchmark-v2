def submatrix_with_particular_sum(matrix):
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            for k in range(len(matrix[0])):
                for l in range(k + 1, len(matrix[0])):
                    if sum(matrix[i:j + 1, k:l + 1].flatten()) == -83:
                        return [matrix[i:j + 1, k:l + 1]]
    return []