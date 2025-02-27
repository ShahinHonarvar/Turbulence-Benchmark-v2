import numpy as np

def submatrix_with_particular_sum(matrix):
    """
    This function takes a two-dimensional numpy array and returns a list of submatrices sums to -10.
    """
    list_of_particular_sums = list()
    for k in range(len(matrix) + 1):
        for i in range(len(matrix) - k + 1):
            for j in range(len(matrix) - k + 1):
                submatrix = matrix[i:i + k, j:j + k]
                if submatrix.sum() == -10:
                    list_of_particular_sums.append(submatrix)
    return list_of_particular_sums