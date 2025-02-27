from typing import List, Tuple
import numpy as np

def submatrix_with_particular_sum(matrix: np.ndarray) -> List[Tuple[int, int, int, int]]:
    """
    Write a function called 'submatrix_with_particular_sum' that takes one argument which is a two-dimensional numpy matrix of integers. The function should return the list of all submatrices of the given matrix such that the sum of all integers in each submatrix equals 54. If no such submatrix is found, the function should return an empty list.
    """
    submatrices: List[Tuple[int, int, int, int]] = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for k in range(i, matrix.shape[0]):
                for l in range(j, matrix.shape[1]):
                    submatrix: np.ndarray = matrix[i:k + 1, j:l + 1]
                    if submatrix.sum() == 54:
                        submatrices.append((i, j, k, l))
    return submatrices