import numpy as np
from numpy.lib.arraysetops import in1d

def submatrix_with_particular_sum(matrix):
    size = np.array(matrix.shape)
    submatrix_list = list()
    for i in range(size[0]):
        for j in range(size[1]):
            for x in range(i + 1, size[0]):
                for y in range(j + 1, size[1]):
                    sub_matrix = matrix[i:x, j:y]
                    if sub_matrix.sum() == 80 and (not in1d(sub_matrix, submatrix_list)):
                        submatrix_list.append(sub_matrix)
    return submatrix_list