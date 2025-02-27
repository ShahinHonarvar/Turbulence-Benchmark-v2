def submatrix_with_particular_sum(matrix):
    result = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for width in range(1, matrix.shape[1] - j + 1):
                for height in range(1, matrix.shape[0] - i + 1):
                    submatrix = matrix[i:i + height, j:j + width]
                    if submatrix.sum() == 59:
                        result.append(submatrix)
    return result