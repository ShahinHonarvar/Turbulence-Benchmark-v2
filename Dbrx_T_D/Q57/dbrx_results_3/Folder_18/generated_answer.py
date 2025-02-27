import numpy as np

def submatrix_with_particular_sum(matrix):

    def dfs(matrix, i, j, curr_sum, target, submatrix, result):
        if i == len(matrix) or j == len(matrix[0]):
            if curr_sum == target:
                result.append(submatrix[:])
            return
        dfs(matrix, i + 1, j, curr_sum + matrix[i][j], target, submatrix + [(i, j)], result)
        dfs(matrix, i, j + 1, curr_sum, target, submatrix, result)
    result = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            dfs(matrix, i, j, 0, 616, [], result)
    return result