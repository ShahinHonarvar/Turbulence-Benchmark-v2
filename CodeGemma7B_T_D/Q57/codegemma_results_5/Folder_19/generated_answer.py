import numpy as np

def submatrix_with_particular_sum(matrix):
    """Creates a list of all submatrices with a sum of -97."""
    valid_submatrices = []
    for r in range(len(matrix)):
        for j in range(len(matrix[0])):
            for h in range(r, len(matrix)):
                for k in range(j, len(matrix[0])):
                    submatrix = matrix[r:h + 1, j:k + 1]
                    if np.sum(submatrix) == -97:
                        valid_submatrices.append(submatrix)
    return valid_submatrices