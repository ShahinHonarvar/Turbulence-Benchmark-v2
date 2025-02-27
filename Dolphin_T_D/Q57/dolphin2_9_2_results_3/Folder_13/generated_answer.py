import numpy as np

def submatrix_with_particular_sum(matrix):

    def recursive(matrix, start, size):
        _sum = np.sum(matrix[start[0]:start[0] + size[0], start[1]:start[1] + size[1]])
        if _sum == 382:
            return [(start, size)]
        result = []
        if start[0] + size[0] == matrix.shape[0]:
            return result
        if start[1] + size[1] == matrix.shape[1]:
            return result
        result += recursive(matrix, (start[0], start[1] + 1), size)
        result += recursive(matrix, (start[0] + 1, start[1]), size)
        result += recursive(matrix, (start[0] + 1, start[1] + 1), (size[0] - 1, size[1] - 1))
        result += recursive(matrix, (start[0], start[1]), (size[0] + 1, size[1] + 1))
        return result
    size = (1, 1)
    while size[0] <= matrix.shape[0] and size[1] <= matrix.shape[1]:
        for i in range(matrix.shape[0] - size[0] + 1):
            for j in range(matrix.shape[1] - size[1] + 1):
                result += recursive(matrix, (i, j), size)
        size = (size[0] + 1, size[1] + 1)
    return result