import numpy as np

def submatrix_with_particular_sum(matrix: np.ndarray) -> list[list[int]]:
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            for k in range(len(matrix[0])):
                for l in range(k, len(matrix[0])):
                    submatrix = matrix[i:j + 1, k:l + 1]
                    sum_of_submatrix = submatrix.sum()
                    if sum_of_submatrix == 54:
                        return [[element for row in submatrix for element in row]]
    return []