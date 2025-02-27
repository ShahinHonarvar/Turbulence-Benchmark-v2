import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            for k in range(len(matrix[0])):
                for l in range(k + 1, len(matrix[0])):
                    temp_sum = 0
                    for m in range(i, j + 1):
                        for n in range(k, l + 1):
                            temp_sum += matrix[m][n]
                    if temp_sum == 57:
                        count += 1
    return count