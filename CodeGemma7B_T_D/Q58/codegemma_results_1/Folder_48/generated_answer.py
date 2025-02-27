import numpy as np

def submatrix_with_n_numbers(matrix):
    """
            Function to count the number of submatrices with n numbers
            """
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 130:
                submatrix = matrix[i:j + 1, j:j + 1]
                if len(np.unique(submatrix)) == 1 and submatrix.size == 130:
                    count += 1
    return count