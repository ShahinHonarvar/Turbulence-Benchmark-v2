def submatrix_with_particular_sum(matrix):
    """
            This function takes a two-dimensional numpy matrix of integers and returns the list of all submatrices of the given matrix such that the sum of all integers in each submatrix equals 17. If no such submatrix is found, the function should return an empty list.
            """
    submatrices = []
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix) + 1):
            for k in range(len(matrix[0])):
                for l in range(k + 1, len(matrix[0]) + 1):
                    submatrix = matrix[i:j, k:l]
                    if np.sum(submatrix) == 17:
                        submatrices.append(submatrix)
    return submatrices