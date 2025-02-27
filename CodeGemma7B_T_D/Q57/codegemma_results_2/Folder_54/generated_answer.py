import numpy as np

def submatrix_with_particular_sum(matrix):
    """
            The following code snippet provides a function called submatrix_with_particular_sum that takes a two-dimensional numpy matrix of integers as an input and returns a list of all submatrices of the given matrix such that the sum of all integers in each submatrix equals -59.

            Parameters:
            matrix: A two-dimensional numpy matrix of integers.

            Returns:
            A list of all submatrices of the given matrix such that the sum of all integers in each submatrix equals -59. If no such submatrix is found, the function should return an empty list.
            """
    sum_left_to_right = np.cumsum(matrix, axis=1)
    sum_top_to_bottom = np.cumsum(sum_left_to_right, axis=0)
    output = []
    for left in range(matrix.shape[1]):
        for right in range(left, matrix.shape[1]):
            for top in range(matrix.shape[0]):
                for bottom in range(top, matrix.shape[0]):
                    current_sum = sum_top_to_bottom[bottom + 1, right + 1] - sum_top_to_bottom[top, right + 1] - sum_top_to_bottom[bottom + 1, left] + sum_top_to_bottom[top, left]
                    if current_sum == -59:
                        output.append((left, top, right, bottom))
    return output