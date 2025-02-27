import numpy as np

def submatrix_with_particular_sum(matrix):
    sum_dict = {}
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            submatrix_sum = matrix[row][col]
            for row2 in range(row + 1, len(matrix)):
                for col2 in range(col + 1, len(matrix[0])):
                    submatrix_sum += matrix[row2][col2]
                    if submatrix_sum == -863:
                        if submatrix_sum not in sum_dict:
                            sum_dict[submatrix_sum] = []
                        sum_dict[submatrix_sum].append((row, col, row2, col2))
    return sum_dict.get(-863, [])