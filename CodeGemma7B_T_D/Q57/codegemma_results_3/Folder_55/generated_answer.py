def submatrix_with_particular_sum(given_matrix):
    """
    :type given_matrix: np.ndarray
    :rtype: list
    """
    submatrix_list = []
    for i in range(len(given_matrix)):
        for j in range(len(given_matrix[0])):
            for k in range(i, len(given_matrix)):
                for l in range(j, len(given_matrix[0])):
                    submatrix = given_matrix[i:k + 1, j:l + 1]
                    if submatrix.sum() == 1:
                        submatrix_list.append(submatrix)
    return submatrix_list