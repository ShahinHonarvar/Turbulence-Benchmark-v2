def submatrix_with_particular_sum(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix[0])):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if submatrix.sum() == -87:
                        return submatrix.tolist()
    return []