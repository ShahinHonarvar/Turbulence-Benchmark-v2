import numpy as np

def submatrix_with_particular_sum(matrix):
    """Finds all submatrices of a given matrix with a sum of 3."""
    ans = []
    for row1 in range(len(matrix)):
        for row2 in range(row1, len(matrix)):
            for col1 in range(len(matrix[0])):
                for col2 in range(col1, len(matrix[0])):
                    sum = 0
                    for r in range(row1, row2 + 1):
                        for c in range(col1, col2 + 1):
                            sum += matrix[r][c]
                    if sum == 3:
                        ans.append([r1 for r1 in range(row1, row2 + 1) for c1 in range(col1, col2 + 1)])
    return ans