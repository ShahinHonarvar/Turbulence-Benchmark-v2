import numpy as np

def submatrix_with_particular_sum(matrix):
    """
  Finds all submatrices of a given matrix with a sum of 100.
  """
    submatrices = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(i + 1, len(matrix)):
                for l in range(j + 1, len(matrix[0])):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if np.sum(submatrix) == 100:
                        submatrices.append(submatrix)
    return submatrices