import numpy as np

def submatrix_with_particular_sum(matrix):
    size_x = len(matrix)
    size_y = len(matrix[0])
    content = -255
    for x in range(size_x):
        for y in range(size_y):
            for size_x2 in range(size_x - x + 1):
                for size_y2 in range(size_y - y + 1):
                    submatrix_sum = np.sum(matrix[x:x + size_x2, y:y + size_y2])
                    if submatrix_sum == content:
                        return matrix[x:x + size_x2, y:y + size_y2]
    return []