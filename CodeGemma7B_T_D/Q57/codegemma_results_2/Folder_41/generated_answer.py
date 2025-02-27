def submatrix_with_particular_sum(matrix):
    """
    This function takes a 2D numpy matrix and returns a list of all submatrices of the given matrix with a sum of -26.
    """
    submatrices = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for k in range(i, matrix.shape[0]):
                for l in range(j, matrix.shape[1]):
                    if sum(matrix[i:k + 1, j:l + 1].flatten()) == -26:
                        submatrices.append(matrix[i:k + 1, j:l + 1])
    return submatrices