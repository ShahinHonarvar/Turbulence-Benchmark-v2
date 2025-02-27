import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for n in range(min(len(matrix) - i + 1, len(matrix[0]) - j + 1)):
                if sum(matrix[i:i + n, j:j + n]) == 139:
                    count += 1
    return count