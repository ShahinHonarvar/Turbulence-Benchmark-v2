import numpy as np

def submatrix_with_n_numbers(matrix):
    """
    Counts the number of submatrices of the given matrix that contain 107 integers each.

    Args:
        matrix: A two-dimensional numpy matrix of integers.

    Returns:
        The count of submatrices of the given matrix that contain 107 integers each.
    """
    matrix_copy = np.copy(matrix)
    mask = matrix_copy == 107
    indices = np.argwhere(mask)
    indices = indices[indices[:, 0].argsort()]
    indices = indices[indices[:, 1].argsort()]
    if len(indices) >= 107:
        stack = []
        count = 0
        for row, col in indices:
            if not stack or (row != stack[-1][0] and col != stack[-1][1]):
                stack.append((row, col))
            if len(stack) >= 107:
                count += 1
            while len(stack) >= 2 and (row != stack[-2][0] and col != stack[-2][1]):
                stack.pop()
        return count
    return 0