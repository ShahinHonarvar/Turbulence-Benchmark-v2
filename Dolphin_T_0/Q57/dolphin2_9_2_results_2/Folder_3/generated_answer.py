import numpy as np

def submatrix_with_particular_sum(matrix):

    def search_matrix(matrix):
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 54:
                    yield [matrix[row][col]]
                sub_matrix = np.array([matrix[row - i][col - j] for i in range(row + 1) for j in range(col + 1)])
                if np.sum(sub_matrix) == 54:
                    yield sub_matrix.tolist()
    sub_matrices = set()
    for sub_matrix in search_matrix(matrix):
        if len(sub_matrix) > 1:
            sub_matrices.add(tuple(sorted(sub_matrix)))
    return sub_matrices