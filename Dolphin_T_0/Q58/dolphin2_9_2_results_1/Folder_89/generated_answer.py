import numpy as np

def submatrix_with_n_numbers(matrix):
    """
    This function takes in a 2D numpy matrix of integers and returns the count of all submatrices of the given matrix that contain 18 integers each. If no submatrix with 18 integers is found, it returns 0.
    """
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for sub_rows in range(3, rows - i + 1):
                for sub_cols in range(6, cols - j + 1):
                    submatrix = matrix[i:i + sub_rows, j:j + sub_cols]
                    if np.sum(submatrix) == 18:
                        count += 1
    return count