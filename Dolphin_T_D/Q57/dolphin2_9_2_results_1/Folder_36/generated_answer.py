import numpy as np
from itertools import product

def submatrix_with_particular_sum(matrix):
    h, w = matrix.shape
    submatrices = []
    for h1, h2 in product(range(h), repeat=2):
        for w1, w2 in product(range(w), repeat=2):
            if sum((matrix[i, j] for i in range(h1, h2) for j in range(w1, w2))) == -779:
                submatrices.append(matrix[h1:h2, w1:w2])
    return submatrices