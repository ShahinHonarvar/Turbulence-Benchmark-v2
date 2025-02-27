from numpy import sum

def submatrix_with_particular_sum(matrix):
    """
    Finds all submatrices of the given matrix with a given sum.

    Args:
        matrix: A two-dimensional numpy matrix of integers.

    Returns:
        A list of all submatrices with the given sum.
    """
    submatrices = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix[0])):
                    submatrix_sum = sum((sum(row[j:l + 1]) for row in matrix[i:k + 1]))
                    if submatrix_sum == -93:
                        submatrices.append((i, j, k, l))
    return submatrices