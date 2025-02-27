import numpy as np

def submatrix_with_particular_sum(matrix):
    """
  Returns list with all submatrices of matrix with sum = 38.
  """
    ans = []
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            for k in range(len(matrix[0])):
                for l in range(k, len(matrix[0])):
                    submatrix = matrix[i:j + 1, k:l + 1]
                    if submatrix.sum() == 38:
                        ans.append(submatrix)
    return ans