from itertools import combinations

def submatrix_with_particular_sum(matrix):
    """
    Returns all submatrices of a 2D numpy matrix with a sum of 80.

    Args:
    matrix: A 2D numpy matrix of integers.

    Returns:
    A list of all submatrices with a sum of 80, or an empty list if no such submatrix is found.
    """

    def all_submatrices(matrix):
        return [(matrix[r1:r2 + 1, c1:c2 + 1] for r1, r2 in combinations(range(rows), 2) for c1, c2 in combinations(range(cols), 2))]
    rows, cols = matrix.shape
    submatrices = [matrix for matrix in all_submatrices(matrix) if matrix.sum() == 80]
    if not submatrices:
        return []
    return submatrices