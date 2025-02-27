import numpy as np

def submatrix_with_particular_sum(matrix):
    """Return a list of all submatrices of the given matrix such that the sum of all integers in each submatrix equals -26.
    """
    list_of_all_submatrix = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for x in range(matrix.shape[0]):
                for y in range(matrix.shape[1]):
                    submatrix = matrix[i:x + 1, j:y + 1]
                    if np.sum(submatrix) == -26:
                        list_of_all_submatrix.append(submatrix)
    return list_of_all_submatrix