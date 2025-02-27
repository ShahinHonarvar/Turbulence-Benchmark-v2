def submatrix_with_particular_sum(matrix):
    result = []
    for i1 in range(len(matrix)):
        for i2 in range(i1 + 1, len(matrix)):
            for j1 in range(len(matrix[0])):
                for j2 in range(j1 + 1, len(matrix[0])):
                    submatrix = matrix[i1:i2 + 1, j1:j2 + 1]
                    if submatrix.sum() == -936:
                        result.append(submatrix)
    return result