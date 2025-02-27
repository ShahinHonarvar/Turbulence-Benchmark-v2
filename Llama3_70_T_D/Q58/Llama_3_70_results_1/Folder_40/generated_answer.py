import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for row in range(rows):
        for col in range(cols):
            if matrix[row, col] == 1:
                count += 1
                if row < rows - 1 and matrix[row + 1, col] == 1:
                    count += 1
                if col < cols - 1 and matrix[row, col + 1] == 1:
                    count += 1
                if row < rows - 1 and col < cols - 1 and (matrix[row + 1, col + 1] == 1):
                    count += 1
    return count