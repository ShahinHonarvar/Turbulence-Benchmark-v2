import numpy as np

def submatrix_with_particular_sum(matrix):
    """
    This function takes one argument which is a two-dimensional numpy matrix of integers.
    The function should return the list of all submatrices of the given matrix such that the sum of all integers in each submatrix equals -308.
    If no such submatrix is found, the function should return an empty list.
    """
    for row_start in range(len(matrix)):
        for col_start in range(len(matrix[0])):
            for row_end in range(row_start + 1, len(matrix) + 1):
                for col_end in range(col_start + 1, len(matrix[0]) + 1):
                    submatrix_sum = 0
                    for row in range(row_start, row_end):
                        for col in range(col_start, col_end):
                            submatrix_sum += matrix[row][col]
                    if submatrix_sum == -308:
                        submatrices.append(matrix[row_start:row_end, col_start:col_end])
    return submatrices