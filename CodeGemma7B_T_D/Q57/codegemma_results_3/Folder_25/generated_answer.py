def submatrix_with_particular_sum(matrix):
    solutions = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            for k in range(i + 1, len(matrix)):
                for l in range(j + 1, len(matrix)):
                    if sum(matrix[i:k + 1][j:l + 1]) == -20:
                        solutions.append(matrix[i:k + 1][j:l + 1])
    if len(solutions) == 0:
        return []
    return solutions