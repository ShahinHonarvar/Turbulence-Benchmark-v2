def submatrix_with_n_numbers(matrix):
    """
    This function takes one argument which is a two-dimensional numpy matrix of integers. The function should return the count of
    all submatrices of the given matrix that contain 111 integers each. If no such submatrix is found, the
    function should return 0.
    """
    count = 0
    size = len(matrix)
    for i in range(size):
        for j in range(size):
            for k in range(i, size):
                for l in range(j, size):
                    if matrix[i:k + 1, j:l + 1].sum() == 111:
                        count += 1
    return count