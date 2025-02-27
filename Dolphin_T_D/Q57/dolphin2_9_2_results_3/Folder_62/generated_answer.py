import numpy as np

def submatrix_with_particular_sum(matrix):
    list_of_submatrices = []
    height, width = matrix.shape
    for i in range(height):
        for j in range(width):
            for height_sub in range(i + 1, height + 1):
                for width_sub in range(j + 1, width + 1):
                    submatrix = matrix[i:height_sub, j:width_sub]
                    if np.sum(submatrix) == 394:
                        list_of_submatrices.append((i, j, height_sub, width_sub))
    return list_of_submatrices