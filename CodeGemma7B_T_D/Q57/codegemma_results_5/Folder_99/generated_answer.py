def submatrix_with_particular_sum(matrix):
    submatrices = []
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            for r2 in range(r, len(matrix)):
                for c2 in range(c, len(matrix[0])):
                    submatrix_sum = 0
                    for i in range(r, r2 + 1):
                        for j in range(c, c2 + 1):
                            submatrix_sum += matrix[i][j]
                    if submatrix_sum == -185:
                        submatrices.append((r, c, r2, c2))
    return submatrices