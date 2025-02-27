import numpy as np

def submatrix_with_particular_sum(matrix):
    sums = matrix.sum(axis=0).sum(axis=0)
    if 80 in sums:
        return [matrix]
    else:
        return []