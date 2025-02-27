import numpy as np

def submatrix_with_n_numbers(matrix):
    length = len(matrix)
    width = len(matrix[0])
    count = 0
    for i in range(length - 1):
        for j in range(width - 1):
            if sum(matrix[i:i + 2, j:j + 2].flatten()) == 8:
                count += 1
    return count