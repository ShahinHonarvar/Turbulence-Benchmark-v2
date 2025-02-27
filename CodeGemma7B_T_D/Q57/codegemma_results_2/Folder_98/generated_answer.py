from typing import List
import numpy as np

def submatrix_with_particular_sum(matrix: np.ndarray) -> List[np.ndarray]:
    """
    The function submatrix_with_particular_sum is an algorithm to find all submatrices of a given matrix with the specific condition that the sum of all integers in each submatrix equals 0.

    Args:
    matrix: The numpy matrix of integers.

    Returns:
    List of all submatrices of the matrix with the specific condition. If such submatrices are not found, the function returns an empty list.
    """
    answer_list = []
    list_matrix = []
    for rows in range(len(matrix)):
        for col in range(len(matrix[0])):
            list_matrix.append(matrix[rows][col])
    for i in range(0, len(list_matrix)):
        for j in range(i + 1, len(list_matrix) + 1):
            submatrix = np.array(list_matrix[i:j])
            if submatrix.sum() == 0:
                answer_list.append(submatrix)
        if answer_list:
            return answer_list
    return answer_list