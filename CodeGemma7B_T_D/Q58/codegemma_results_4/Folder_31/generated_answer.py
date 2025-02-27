import numpy as np

def submatrix_with_n_numbers(matrix):
    size = matrix.shape[0]
    number = matrix.shape[1]
    count = 0
    for i in range(size):
        for j in range(number):
            for x in range(i, size):
                for y in range(j, number):
                    temp = matrix[i:x + 1, j:y + 1]
                    if temp.size == 45:
                        count += 1
    return count