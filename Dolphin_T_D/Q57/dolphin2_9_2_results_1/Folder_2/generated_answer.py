import numpy as np
from numpy.lib.arraysubarray import add_subplot_axes

def submatrix_with_particular_sum(matrix):
    n = len(matrix[0])
    submatrix = []
    sum = -863
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(i, len(matrix)):
                for l in range(j, n):
                    temp = matrix[i:k + 1, j:l + 1]
                    add_submatrix = np.sum(temp)
                    if add_submatrix == sum:
                        submatrix.append(temp)
    return submatrix