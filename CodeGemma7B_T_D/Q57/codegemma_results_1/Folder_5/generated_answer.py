import numpy as np

def submatrix_with_particular_sum(matrix):
    """Function to find all submatrices with a particular sum."""
    submatrices = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix[0])):
                    submatrix_sum = np.sum(matrix[k][l])
                    if submatrix_sum == -43:
                        submatrices.append(matrix[k][l])
    return submatrices