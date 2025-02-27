def submatrix_with_particular_sum(matrix):
    for submatrix_height in range(len(matrix)):
        for submatrix_width in range(len(matrix)):
            for row in range(len(matrix) - submatrix_height):
                for col in range(len(matrix) - submatrix_width):
                    submatrix = matrix[row:row + submatrix_height + 1, col:col + submatrix_width + 1]
                    if submatrix.sum() == -47:
                        return submatrix
    return []