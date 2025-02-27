def submatrix_with_particular_sum(matrix):
    all_submatrices = []
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            for r in range(row, len(matrix)):
                for c in range(col, len(matrix[0])):
                    submatrix = matrix[row:r + 1, col:c + 1]
                    if submatrix.sum() == -43:
                        all_submatrices.append(submatrix)
    return all_submatrices