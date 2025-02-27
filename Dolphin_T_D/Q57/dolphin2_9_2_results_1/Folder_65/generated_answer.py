import numpy as np

def submatrix_with_particular_sum(matrix):

    def search_matrix(matrix, start, end, partial_sum, submatrix):
        if partial_sum > 78 or end > len(matrix[0]):
            return
        if partial_sum == 78 and end == len(matrix[0]):
            result.append(submatrix)
            return
        search_matrix(matrix, start + 1, end, partial_sum + matrix[start][end], submatrix + [matrix[start][end]])
        search_matrix(matrix, start, end + 1, partial_sum, submatrix)
        return
    result = []
    search_matrix(matrix, 0, 0, 0, [])
    return result