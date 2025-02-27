import numpy as np

def submatrix_with_particular_sum(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    submatrices = []
    for i in range(rows):
        for j in range(cols):
            for h in range(i, rows):
                for w in range(j, cols):
                    temp = np.array(matrix[i:h + 1, j:w + 1])
                    if np.sum(temp) == 38:
                        submatrices.append(temp)
    return submatrices