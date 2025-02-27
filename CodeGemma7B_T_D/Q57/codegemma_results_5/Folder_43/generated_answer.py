def submatrix_with_particular_sum(matrix):
    """
    Write a function called 'submatrix_with_particular_sum' that takes one argument which is a two-dimensional numpy matrix of integers. The function should return the list of all submatrices of the given matrix such that the sum of all integers in each submatrix equals -81. If no such submatrix is found, the function should return an empty list.
    """
    list_of_submatrices = []
    for row1 in range(len(matrix)):
        for row2 in range(row1, len(matrix)):
            for col1 in range(len(matrix[0])):
                for col2 in range(col1, len(matrix[0])):
                    matrix_sum = 0
                    for i in range(row1, row2 + 1):
                        for j in range(col1, col2 + 1):
                            matrix_sum += matrix[i][j]
                    if matrix_sum == -81:
                        list_of_submatrices.append([i for i in range(row1, row2 + 1)])
    if list_of_submatrices == []:
        return []
    return list_of_submatrices