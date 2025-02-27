def submatrix_with_particular_sum(matrix):
    """
    Returns a list of all submatrices of the given matrix such that the sum of all integers in each submatrix equals 78.
    """
    submatrices = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix[0])):
                    if sum((row[j:l + 1] for row in matrix[i:k + 1])) == 78:
                        submatrices.append((i, j, k, l))
    return submatrices