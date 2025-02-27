def submatrix_with_particular_sum(mat):
    """
    This function returns the list of all submatrices of a given matrix such that the sum of all integers in each submatrix equals the target sum.

    Parameters:
    -----------
    mat : numpy.ndarray
        A 2-dimensional numpy array of integers.

    Returns:
    --------
    list
        A list of submatrices such that the sum of all integers in each submatrix equals the target sum. If no submatrix is found, an empty list is returned.
    """
    target_sum = 16
    result = []
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            for k in range(i, len(mat)):
                for l in range(j, len(mat[0])):
                    submatrix = mat[i:k + 1, j:l + 1]
                    if submatrix.sum() == target_sum:
                        result.append(submatrix)
    return result