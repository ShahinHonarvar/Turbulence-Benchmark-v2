def submatrix_with_particular_sum(matrix):
    """
    Submatrix with particular sum
    """
    submatrices = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix)):
                    submatrix = matrix[i:l + 1, j:k + 1]
                    if submatrix.sum() == -64:
                        submatrices.append(submatrix)
    return submatrices