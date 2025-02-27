def submatrix_with_particular_sum(matrix):
    for x in range(len(matrix)):
        for y in range(x + 1, len(matrix)):
            for a in range(len(matrix[0])):
                for b in range(a + 1, len(matrix[0])):
                    submat = matrix[x:y + 1, a:b + 1]
                    if submat.sum() == -46:
                        return [submat]
    return []