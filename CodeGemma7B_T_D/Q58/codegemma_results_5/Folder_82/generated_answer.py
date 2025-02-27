import numpy as np

def submatrix_with_n_numbers(matrix):
    """
    This function takes a 2D numpy matrix of integers and returns the count of all submatrices with 99 integers each.

    The submatrices are counted based on the rows and columns of the matrix. The first value of the input array is the number of rows in the matrix. The second value of the input array is the number of columns in the matrix.

    The function returns 0 if no submatrix with n numbers of 99 is found.
    """
    rows, cols = matrix.shape
    count = 0
    for row in range(rows):
        for col in range(cols):
            if matrix[row, col] == 99:
                for r in range(row, rows):
                    for c in range(col, cols):
                        if matrix[r, c] == 99:
                            count += 1
    return count