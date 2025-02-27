import numpy as np

def submatrix_with_particular_sum(matrix):
    """
  Takes one argument which is a two-dimensional numpy matrix of integers.
  The function returns the list of all submatrices of the given matrix such that the sum of all integers
  in each submatrix equals -128. If no such submatrix is found, the function should return an empty list.
  """
    nums = set()
    nums.add(0)
    for i in range(len(matrix)):
        rowSum = 0
        for j in range(len(matrix[0])):
            rowSum += matrix[i][j]
            nums.add(rowSum)
            if rowSum - 128 in nums:
                answer.append([matrix[i][start:j + 1] for start in range(i)])
    return answer