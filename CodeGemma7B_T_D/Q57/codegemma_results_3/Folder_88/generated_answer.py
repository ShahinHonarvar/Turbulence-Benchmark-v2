def submatrix_with_particular_sum(matrix):
    """
             Submatrix with particular sum function.

             Args:
             matrix: A 2-dimensional numpy matrix of integers.

             Returns:
             A list of all submatrices with the given sum.
            """
    rows = matrix.shape[0]
    cols = matrix.shape[1]
    submatrices = []
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    submatrix_sum = submatrix.sum()
                    if submatrix_sum == -64:
                        submatrices.append(submatrix)
    return submatrices