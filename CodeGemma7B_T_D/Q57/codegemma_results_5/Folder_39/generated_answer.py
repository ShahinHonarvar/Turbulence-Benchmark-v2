def submatrix_with_particular_sum(matrix):
    """
            Write a function called 'submatrix_with_particular_sum' that takes one argument which is a two-dimensional numpy matrix of integers. The function should return the list of all submatrices of the given matrix such that the sum of all integers in each submatrix equals 66. If no such submatrix is found, the function should return an empty list.
            """
    '\n            To find submatrices with a particular sum, we can iterate through the matrix and use the two-pointer technique. We can define two pointers, one for the starting row of the submatrix and another for the ending row. We can move these pointers iteratively, keeping track of the sum of integers in the current submatrix. If the sum matches the desired sum, we can add the submatrix to the list of result submatrices.\n            '
    result = []
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            submatrix = matrix[i:j + 1]
            current_sum = 0
            for row in submatrix:
                current_sum += sum(row)
            if current_sum == 66:
                result.append(submatrix)
    return result