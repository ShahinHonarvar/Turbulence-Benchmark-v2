import numpy as np
from itertools import product  # itertools product tool helps generate pairs of rows and columns to generate our submatrices.

def submatrix_with_n_numbers(matrix):
    count = 0
    for r1, r2 in product(range(len(matrix)), repeat=2):
        for c1, c2 in product(range(len(matrix[0])), repeat=2):
            if r2 >= r1 and c2 >= c1:
                submatrix = matrix[r1:r2 + 1, c1:c2 + 1]
                if len(submatrix) * len(submatrix[0]) == 146:
                    count += 1
    return count