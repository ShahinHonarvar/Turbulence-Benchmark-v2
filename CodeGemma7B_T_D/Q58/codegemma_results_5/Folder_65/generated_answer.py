def submatrix_with_n_numbers(matrix):
    """
    Write a function called 'submatrix_with_n_numbers' that takes one argument which is a two-dimensional numpy matrix of integers. The function should return the count of all submatrices of the given matrix that contain 35 integers each. If no such submatrix is found, the function should return 0.
    """
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(i + 1, len(matrix)):
                for l in range(j + 1, len(matrix[0])):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if submatrix.shape[0] * submatrix.shape[1] == 35:
                        count += 1
    return count