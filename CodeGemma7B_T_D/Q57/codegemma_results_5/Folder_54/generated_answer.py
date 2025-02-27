import numpy as np

def submatrix_with_particular_sum(matrix):
    """ This function takes a two-dimensional numpy matrix of integers as an argument.
  It returns the list of all submatrices of the given matrix such that the sum of all integers in each submatrix equals -59.
  If no such submatrix is found, the function should return an empty list.
  """
    result = []

    def checkSum(matrices):
        for matrix in matrices:
            if sum((sum(row) for row in matrix)) == -59:
                return matrix
        return []
    left, right = (0, len(matrix[0]))
    for top in range(len(matrix)):
        for down in range(top, len(matrix)):
            for left in range(len(matrix[0])):
                for right in range(left, len(matrix[0])):
                    submatrix = matrix[top:down + 1, left:right + 1]
                    result.append(submatrix)
    return checkSum(result)