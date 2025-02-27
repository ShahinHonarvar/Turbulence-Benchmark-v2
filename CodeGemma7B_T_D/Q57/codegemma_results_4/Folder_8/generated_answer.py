import numpy as np

def submatrix_with_particular_sum(matrix):
    """Function to find all submatrices with a specific sum."""
    sum_to_find = -61
    all_submatrices = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix[0])):
                    Submatrix = matrix[i:k + 1, j:l + 1]
                    if np.sum(Submatrix) == sum_to_find:
                        all_submatrices.append(Submatrix)
    return all_submatrices