import numpy as np

def submatrix_with_particular_sum(matrix):
    list_of_submatrices = []
    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
            if matrix[row][column] == -36:
                list_of_submatrices.append(matrix[row][column])
            else:
                current_sum = 0
                for i in range(row, len(matrix)):
                    for j in range(column, len(matrix[0])):
                        current_sum += matrix[i][j]
                        if current_sum == -36:
                            list_of_submatrices.append(matrix[row:i + 1, column:j + 1])
                        elif current_sum > -36:
                            break
    return list_of_submatrices