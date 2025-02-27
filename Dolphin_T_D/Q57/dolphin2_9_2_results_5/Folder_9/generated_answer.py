import numpy as np
from itertools import product

def submatrix_with_particular_sum(matrix):
    index_sets = list(product(range(matrix.shape[0]), range(matrix.shape[1])))
    submatrices = []
    for index1 in index_sets:
        for index2 in index_sets:
            if index1[0] > index2[0] and index1[1] > index2[1]:
                submatrix_sum = np.sum(matrix[index1[0]:index2[0] + 1, index1[1]:index2[1] + 1])
                if submatrix_sum == -86:
                    submatrices.append(matrix[index1[0]:index2[0] + 1, index1[1]:index2[1] + 1])
    return submatrices