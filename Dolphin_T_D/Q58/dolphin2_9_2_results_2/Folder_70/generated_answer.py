import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    a, b = matrix.shape
    for i in range(a):
        for j in range(b):
            for k in range(i + 1, a):
                for l in range(j + 1, b):
                    submatrix = matrix[i:k, j:l]
                    if len(submatrix) == 173:
                        count += 1
    if count == 0:
        return 0
    else:
        return count