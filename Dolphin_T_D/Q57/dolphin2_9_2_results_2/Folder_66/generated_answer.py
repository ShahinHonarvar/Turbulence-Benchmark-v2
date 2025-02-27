import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    height, width = (len(matrix), len(matrix[0]))
    for i in range(height):
        for j in range(width):
            for dx in range(i, height):
                for dy in range(j, width):
                    submatrix = np.array(matrix[i:dx + 1, j:dy + 1])
                    if submatrix.sum() == 99:
                        result.append(submatrix)
    return result