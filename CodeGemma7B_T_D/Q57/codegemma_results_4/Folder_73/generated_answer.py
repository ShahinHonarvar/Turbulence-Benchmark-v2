def submatrix_with_particular_sum(matrix):
    """
    Write a function called 'submatrix_with_particular_sum' that takes one argument which is a two-dimensional numpy matrix of integers. The function should return the list of all submatrices of the given matrix such that the sum of all integers in each submatrix equals 93. If no such submatrix is found, the function should return an empty list.
    """
    result = []
    for left in range(len(matrix)):
        for right in range(left, len(matrix)):
            for up in range(len(matrix)):
                for down in range(up, len(matrix)):
                    submatrix = matrix[up:down + 1]
                    if all([sum(row) == 93 for row in submatrix]):
                        result.append(matrix[left:right + 1][up:down + 1])
    return result