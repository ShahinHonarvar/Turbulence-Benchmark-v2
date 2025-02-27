import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            for x in range(i + 1, len(matrix)):
                for y in range(j + 1, len(matrix[i])):
                    if len(matrix[i:x + 1, j:y + 1].flatten()) == 17:
                        count += 1
    return count