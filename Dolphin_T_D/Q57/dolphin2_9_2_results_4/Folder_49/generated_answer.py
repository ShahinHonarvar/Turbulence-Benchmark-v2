import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    rows, columns = (len(matrix), len(matrix[0]))
    for i in range(rows):
        for j in range(columns):
            for x in range(i, rows):
                for y in range(j, columns):
                    subarray = matrix[i:x + 1, j:y + 1]
                    if np.sum(subarray) == -42:
                        submatrices.append(subarray)
    return submatrices