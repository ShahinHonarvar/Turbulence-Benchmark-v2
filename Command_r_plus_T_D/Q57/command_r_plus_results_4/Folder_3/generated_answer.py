import numpy as np

def submatrix_with_particular_sum(matrix: np.ndarray) -> list[np.ndarray]:

    def get_submatrices(matrix):
        rows, cols = matrix.shape
        for i in range(rows):
            for j in range(cols):
                for k in range(i + 1, rows + 1):
                    for l in range(j + 1, cols + 1):
                        yield matrix[i:k, j:l]

    def sum_of_submatrix(submatrix):
        return np.sum(submatrix)
    target_sum = 54
    all_submatrices = list(get_submatrices(matrix))
    matching_submatrices = [submatrix for submatrix in all_submatrices if sum_of_submatrix(submatrix) == target_sum]
    return matching_submatrices