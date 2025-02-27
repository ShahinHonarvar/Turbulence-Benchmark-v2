def submatrix_with_particular_sum(matrix):
    """
            Returns a list of all submatrices of the given matrix such that the sum of all integers in each submatrix equals -82.
            """
    if not matrix:
        return []
    result = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for width in range(1, len(matrix) - i + 1):
                for height in range(1, len(matrix[0]) - j + 1):
                    submatrix = matrix[i:i + width, j:j + height]
                    if submatrix.sum() == -82:
                        result.append(submatrix)
    return result