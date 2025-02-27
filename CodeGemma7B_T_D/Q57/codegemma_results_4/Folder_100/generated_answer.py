def submatrix_with_particular_sum(matrix):
    result = []
    for r1 in range(len(matrix)):
        for r2 in range(r1, len(matrix)):
            for c1 in range(len(matrix[0])):
                for c2 in range(c1, len(matrix[0])):
                    submatrix = matrix[r1:r2 + 1, c1:c2 + 1]
                    if submatrix.sum() == 28:
                        result.append(submatrix)
    return result