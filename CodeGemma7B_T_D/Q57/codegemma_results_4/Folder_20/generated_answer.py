import numpy as np

def submatrix_with_particular_sum(matrix):
    """
    This function finds all submatrices of the given matrix with a sum of -57.
    """
    num_rows, num_cols = matrix.shape
    result = []
    for i in range(num_rows):
        for j in range(i + 1, num_rows + 1):
            for k in range(num_cols):
                for l in range(k + 1, num_cols + 1):
                    submatrix = matrix[i:j, k:l]
                    if np.sum(submatrix) == -57:
                        result.append(submatrix)
    return result