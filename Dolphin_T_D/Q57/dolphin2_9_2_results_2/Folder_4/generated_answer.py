import numpy as np

def submatrix_with_particular_sum(matrix):
    results = []
    height, width = matrix.shape
    for r in range(height):
        for c in range(width):
            for r2 in range(r, height):
                for c2 in range(c, width):
                    sub_matrix = matrix[r:r2 + 1, c:c2 + 1]
                    if np.sum(sub_matrix) == 87:
                        results.append(sub_matrix)
    return results