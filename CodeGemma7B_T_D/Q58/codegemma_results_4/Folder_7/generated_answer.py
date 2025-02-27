import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            for row1 in range(row, len(matrix)):
                for col1 in range(col, len(matrix[0])):
                    temp = matrix[row:row1 + 1, col:col1 + 1]
                    if temp.shape[0] * temp.shape[1] == 121 and np.all(temp == 1):
                        count += 1
    return count