import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    total_elements = len(matrix) * len(matrix[0])
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if total_elements - (len(matrix) - i) * (len(matrix[0]) - j) + 1 == 29:
                count += 1
    return count