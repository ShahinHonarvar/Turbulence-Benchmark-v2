import numpy as np

def submatrix_with_n_numbers(matrix):
    """
          Counts the number of submatrices with 28 integers each in a given numpy matrix.

          Args:
            matrix: A two-dimensional numpy matrix of integers.

          Returns:
            The count of submatrices of the given matrix with 28 integers each.
          """
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(i + 1, len(matrix)):
                for l in range(j + 1, len(matrix[0])):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if submatrix.shape[0] >= 4 and submatrix.shape[1] >= 4 and (np.unique(submatrix).size == 28):
                        count += 1
    return count