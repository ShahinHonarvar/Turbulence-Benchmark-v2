def submatrix_with_particular_sum(matrix):
    results = []
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            for height in range(row, len(matrix)):
                for width in range(col, len(matrix[0])):
                    submatrix = matrix[row:height + 1, col:width + 1]
                    if np.sum(submatrix) == -36:
                        results.append(submatrix)
    return results