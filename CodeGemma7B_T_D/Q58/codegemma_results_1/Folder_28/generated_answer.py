from numpy import *

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(i + 1):
                for l in range(j + 1):
                    submatrix = matrix[k:i + 1, l:j + 1]
                    if sum(submatrix.flatten()) == 37:
                        count += 1
    return count