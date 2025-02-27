import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i + 60 <= len(matrix) and j + 60 <= len(matrix[0]):
                submatrix = matrix[i:i + 60, j:j + 60]
                if submatrix.sum() == 60:
                    count += 1
    return count