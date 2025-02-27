import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            for k in range(len(matrix[0])):
                for l in range(k + 1, len(matrix[0])):
                    submatrix = matrix[i:j + 1, k:l + 1]
                    if len(submatrix) * len(submatrix[0]) == 18:
                        count += 1
    return count