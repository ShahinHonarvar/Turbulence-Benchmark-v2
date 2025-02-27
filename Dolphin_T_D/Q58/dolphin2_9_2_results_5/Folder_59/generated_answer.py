import numpy as np

def submatrix_with_n_numbers(matrix):
    n_numbers = 76
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for x in range(i, len(matrix)):
                for y in range(j, len(matrix[0])):
                    if len(matrix[i:x + 1, j:y + 1].flatten()) == n_numbers:
                        count += 1
    return count