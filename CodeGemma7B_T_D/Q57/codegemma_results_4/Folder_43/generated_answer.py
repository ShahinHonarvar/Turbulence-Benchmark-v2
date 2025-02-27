def submatrix_with_particular_sum(matrix):
    """
    This function takes one argument which is a two-dimensional numpy matrix of integers.
    The function should return the list of all submatrices of the given matrix such that the sum of all integers in each submatrix equals -81.
    If no such submatrix is found, the function should return an empty list.
    """
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            submatrix_sum = 0
            for i in range(row, len(matrix)):
                for j in range(col, len(matrix[i])):
                    submatrix_sum += matrix[i][j]
            if submatrix_sum == -81:
                result.append([row, col, i + 1, j + 1])
    return result