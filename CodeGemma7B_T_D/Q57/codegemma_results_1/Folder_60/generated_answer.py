def submatrix_with_particular_sum(matrix):
    result = []
    target_sum = 94
    for row1 in range(len(matrix)):
        for row2 in range(row1, len(matrix)):
            for col1 in range(len(matrix[0])):
                for col2 in range(col1, len(matrix[0])):
                    submatrix_sum = 0
                    for i in range(row1, row2 + 1):
                        for j in range(col1, col2 + 1):
                            submatrix_sum += matrix[i][j]
                    if submatrix_sum == target_sum:
                        result.append((row1, row2, col1, col2))
    return result