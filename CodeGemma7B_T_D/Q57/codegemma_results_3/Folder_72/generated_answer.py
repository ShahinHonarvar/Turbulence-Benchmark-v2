import numpy as np

def submatrix_with_particular_sum(matrix):
    """
            Given a 2D numpy matrix, return a list of all submatrices
            with a sum of 41.
            """
    result = []
    for row_1 in range(len(matrix)):
        for row_2 in range(row_1, len(matrix)):
            for col_1 in range(len(matrix[0])):
                for col_2 in range(col_1, len(matrix[0])):
                    submatrix = matrix[row_1:row_2 + 1, col_1:col_2 + 1]
                    submatrix_sum = np.sum(submatrix)
                    if submatrix_sum == 41:
                        result.append(submatrix)
    return result