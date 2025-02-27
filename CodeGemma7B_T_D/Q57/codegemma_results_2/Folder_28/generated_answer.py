import numpy as np

def submatrix_with_particular_sum(matrix, target_sum):
    """
  Write a function called 'submatrix_with_particular_sum' that takes one argument which is a two-dimensional numpy matrix of integers.
  The function should return the list of all submatrices of the given matrix such that the sum of all integers in each submatrix equals 15.
  If no such submatrix is found, the function should return an empty list.
  """
    rows, cols = matrix.shape
    submatrices = []
    for row in range(rows):
        for col in range(cols):
            for r in range(row, rows):
                for c in range(col, cols):
                    submatrix = matrix[row:r + 1, col:c + 1]
                    if submatrix.sum() == target_sum:
                        submatrices.append(submatrix)
    return submatrices