import numpy as np

def submatrix_with_particular_sum(matrix):
    """
    The function finds all submatrices of the given matrix such that the sum of all integers in each submatrix equals -6. 
    If no such submatrix is found, it returns an empty list.
    """
    submatrices = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(i + 1, len(matrix) + 1):
                for l in range(j + 1, len(matrix[0]) + 1):
                    sum_submatrix = np.sum(matrix[i:k, j:l])
                    if sum_submatrix == -6:
                        submatrices.append(matrix[i:k, j:l])
    return submatrices