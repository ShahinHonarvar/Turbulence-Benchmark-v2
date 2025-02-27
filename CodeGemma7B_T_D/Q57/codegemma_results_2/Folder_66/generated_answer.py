import numpy as np

def submatrix_with_particular_sum(matrix):
    """
  This function finds all submatrices of the given matrix with a sum of 99.
  """
    result = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix[0])):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if submatrix.sum() == 99:
                        result.append(submatrix)
    return result