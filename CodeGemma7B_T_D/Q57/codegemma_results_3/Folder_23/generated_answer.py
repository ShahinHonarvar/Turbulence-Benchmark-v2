import numpy as np

def submatrix_with_particular_sum(matrix):
    """
  This function takes one argument which is a two-dimensional numpy matrix of integers.
  The function should return the list of all submatrices of the given matrix such that the sum of all integers in each submatrix equals 59.
  If no such submatrix is found, the function should return an empty list.
  """
    sum_list = []
    sum_arr = np.zeros(matrix.shape)
    sum_arr[:, :] = matrix == 59
    for row1 in range(matrix.shape[0]):
        for row2 in range(row1, matrix.shape[0]):
            for col1 in range(matrix.shape[1]):
                for col2 in range(col1, matrix.shape[1]):
                    submatrix = []
                    for i in range(row1, row2 + 1):
                        temp = []
                        for j in range(col1, col2 + 1):
                            temp.append(matrix[i][j])
                        submatrix.append(temp)
                    if sum_arr[row1:row2 + 1, col1:col2 + 1].sum() == sum([list(row).count(59) for row in submatrix]):
                        sum_list.append(submatrix)
    return sum_list