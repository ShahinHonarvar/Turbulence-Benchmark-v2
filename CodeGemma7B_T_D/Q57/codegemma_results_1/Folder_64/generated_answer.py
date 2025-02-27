from itertools import product

def submatrix_with_particular_sum(matrix):
    """
  Write a function called 'submatrix_with_particular_sum' that takes one argument which is a two-dimensional numpy matrix of integers. The function should return the list of all submatrices of the given matrix such that the sum of all integers in each submatrix equals -4. If no such submatrix is found, the function should return an empty list.
  """
    rows, cols = matrix.shape
    submatrices = []
    for r1, r2 in product(range(rows), repeat=2):
        if r1 <= r2:
            for c1, c2 in product(range(cols), repeat=2):
                if c1 <= c2:
                    submatrix = matrix[r1:r2 + 1, c1:c2 + 1]
                    if submatrix.sum() == -4:
                        submatrices.append(submatrix)
    return submatrices