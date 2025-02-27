import numpy as np

def submatrix_with_particular_sum(matrix: np.ndarray) -> list[np.ndarray]:

    def get_submatrices(matrix):
        rows, cols = matrix.shape
        for i in range(rows):
            for j in range(cols):
                for k in range(i, rows):
                    for l in range(j, cols):
                        yield matrix[i:k + 1, j:l + 1]

    def sum_of_submatrix(submatrix):
        return np.sum(submatrix)
    result = []
    for submatrix in get_submatrices(matrix):
        if sum_of_submatrix(submatrix) == 21:
            result.append(submatrix)
    return result