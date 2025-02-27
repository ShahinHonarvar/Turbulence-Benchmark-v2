import numpy as np

def submatrix_with_particular_sum(matrix):
    """
            To find all submatrices with the sum of all its integers equal to a specific number.
            """
    count = 0
    for left in range(len(matrix)):
        for right in range(left, len(matrix)):
            for top in range(len(matrix)):
                for bottom in range(top, len(matrix)):
                    submatrix = matrix[top:bottom + 1, left:right + 1]
                    if submatrix.sum() == 40:
                        count += 1
    return count