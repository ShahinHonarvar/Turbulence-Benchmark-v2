import numpy as np

def submatrix_with_n_numbers(matrix):
    """
    This function takes a two-dimensional numpy matrix of integers as an argument.
    The function searches for and returns the count of all submatrices of this matrix which contain 77 integers each.
    If no such submatrix is found, the function returns 0.
    """
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix[0])):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if np.sum(submatrix) == 77 * len(submatrix) and len(submatrix) == l - j + 1 and (len(submatrix[0]) == k - i + 1):
                        count += 1
    return count