import numpy as np

def submatrix_with_n_numbers(matrix):
    """
            The function takes one argument which is a two-dimensional numpy matrix of integers. The function should return the count of all submatrices of the given matrix that contain 94 integers each. If no such submatrix is found, the function should return 0.
            """
    count = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            for r in range(row, len(matrix)):
                for c in range(col, len(matrix[0])):
                    if len(set((matrix[r][c] for r in range(row, r + 1) for c in range(col, c + 1)))) == 94:
                        count += 1
    return count