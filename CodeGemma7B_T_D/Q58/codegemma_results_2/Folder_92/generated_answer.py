import numpy as np

def submatrix_with_n_numbers(matrix):
    """Counts the number of submatrices with n numbers."""
    result = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if col + 8 <= len(matrix[row]):
                for row2 in range(row, row + 9):
                    if row2 >= len(matrix):
                        break
                    if not set(matrix[row2][col:col + 9]).issubset({8}):
                        break
                else:
                    result += 1
    return result