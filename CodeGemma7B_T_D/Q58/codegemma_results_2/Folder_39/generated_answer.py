from numpy import *

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            temp = 0
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix[0])):
                    temp += matrix[k, l]
                    if temp == 59:
                        count += 1
    return count