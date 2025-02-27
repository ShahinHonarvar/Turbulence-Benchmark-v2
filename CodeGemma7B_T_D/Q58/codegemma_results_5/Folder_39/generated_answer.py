import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(i + 1, len(matrix)):
                for l in range(j + 1, len(matrix[0])):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if submatrix.sum() == 59:
                        count += 1
    return count