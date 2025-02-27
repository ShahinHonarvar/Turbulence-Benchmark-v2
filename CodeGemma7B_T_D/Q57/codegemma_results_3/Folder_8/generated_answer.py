import numpy as np

def submatrix_with_particular_sum(matrix):
    list_of_submatrices = []
    for starting_row in range(len(matrix)):
        for ending_row in range(starting_row, len(matrix)):
            for starting_col in range(len(matrix[0])):
                for ending_col in range(starting_col, len(matrix[0])):
                    submatrix = matrix[starting_row:ending_row + 1, starting_col:ending_col + 1]
                    if submatrix.sum() == -61:
                        list_of_submatrices.append(submatrix)
    return list_of_submatrices