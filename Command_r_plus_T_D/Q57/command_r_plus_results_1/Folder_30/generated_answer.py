import numpy as np

def submatrix_with_particular_sum(matrix: np.ndarray) -> list[np.ndarray]:

    def get_submatrices(matrix, rows, cols):
        for i in range(rows):
            for j in range(cols):
                for r in range(i + 1, rows + 1):
                    for c in range(j + 1, cols + 1):
                        yield matrix[i:r, j:c]
    rows, cols = matrix.shape
    submatrices = get_submatrices(matrix, rows, cols)
    target_sum_submatrices = [m for m in submatrices if m.sum() == 21]
    return target_sum_submatrices