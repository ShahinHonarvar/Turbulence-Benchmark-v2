import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    sum_position = {}
    current_sum = 0
    for row in range(matrix.shape[0]):
        for col in range(matrix.shape[1]):
            current_sum += matrix[row][col]
            if current_sum - -87 in sum_position:
                for j in range(sum_position[current_sum - -87] + 1, row + 1):
                    for k in range(col + 1):
                        result.append([row for row in range(j, row + 1)][:][::-1][k:])
            if current_sum not in sum_position:
                sum_position[current_sum] = row
    return result