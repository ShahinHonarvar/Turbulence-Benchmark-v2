def submatrix_with_particular_sum(matrix):
    submatrices = []
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            for r in range(row, len(matrix)):
                for c in range(col, len(matrix[0])):
                    submatrix_sum = 0
                    for i in range(row, r + 1):
                        for j in range(col, c + 1):
                            submatrix_sum += matrix[i][j]
                    if submatrix_sum == 41:
                        submatrices.append((row, col, r, c))
    return submatrices