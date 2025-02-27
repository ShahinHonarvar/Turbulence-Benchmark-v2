def submatrix_with_particular_sum(matrix):
    """
    Finds all submatrices with elements such that their sums are equal to 64.

    Args:
        matrix: A two-dimensional numpy matrix of integers.

    Returns:
        A list of all submatrices with elements such that the sum of all integers in each submatrix equals 64. If no such submatrix is found, return an empty list.
    """
    output = []
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            for r in range(row, len(matrix)):
                for c in range(col, len(matrix[0])):
                    submatrix = matrix[row:r + 1, col:c + 1]
                    output.append(submatrix) if submatrix.sum() == 64 else None
    return output