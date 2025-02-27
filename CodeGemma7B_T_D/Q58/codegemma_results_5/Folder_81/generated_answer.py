from numpy import *

def submatrix_with_n_numbers(matrix):
    count = 0
    for x in range(matrix.shape[0]):
        for y in range(matrix.shape[1]):
            for h in range(0, matrix.shape[0] - x):
                for w in range(0, matrix.shape[1] - y):
                    if (matrix[x:x + h, y:y + w] == 97).all():
                        count += 1
    return count