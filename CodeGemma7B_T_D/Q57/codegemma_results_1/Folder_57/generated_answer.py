import numpy as np

def submatrix_with_particular_sum(matrix):
    number_of_rows, number_of_columns = matrix.shape
    submatrix_sum_should_be = number_of_rows + number_of_columns
    list_of_submatrices = []
    for size_of_submatrix in range(1, number_of_rows + number_of_columns + 1):
        for i in range(number_of_rows - size_of_submatrix + 1):
            for j in range(number_of_columns - size_of_submatrix + 1):
                submatrix = matrix[i:i + size_of_submatrix, j:j + size_of_submatrix]
                if submatrix.sum() == submatrix_sum_should_be:
                    list_of_submatrices.append(submatrix)
    return list_of_submatrices