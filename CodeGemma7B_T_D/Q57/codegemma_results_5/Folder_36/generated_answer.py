from itertools import product
import numpy as np

def submatrix_with_particular_sum(matrix):
    sum_list = []
    for i, j in product(range(matrix.shape[0]), range(matrix.shape[1])):
        summ = 0
        for x, y in product(range(i, matrix.shape[0]), range(j, matrix.shape[1])):
            summ += matrix[x][y]
            if summ == -779:
                sum_list.append(matrix[x][y])
    return sum_list