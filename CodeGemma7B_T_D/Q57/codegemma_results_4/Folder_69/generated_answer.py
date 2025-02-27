import numpy as _numpy

def submatrix_with_particular_sum(_matrix):
    top_range = _numpy.shape(_matrix)[0]
    top_range = top_range - 3
    result_list = []
    for i in range(top_range):
        for j in range(i + 4):
            submatrix = _matrix[i:j, i:j]
            if _numpy.sum(submatrix) == 752:
                result_list.append(submatrix)
    return result_list