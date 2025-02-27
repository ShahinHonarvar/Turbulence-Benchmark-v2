from typing import List
        import numpy as np

def submatrix_with_particular_sum(matrix: np.ndarray) -> List[np.ndarray]:
    """
            This function returns the list of all submatrices of the given matrix
            such that the sum of all integers in each submatrix equals 93.
            """
    res = []
    for r1 in range(len(matrix)):
        for r2 in range(r1, len(matrix)):
            for c1 in range(len(matrix[0])):
                for c2 in range(c1, len(matrix[0])):
                    submatrix = matrix[r1:r2 + 1, c1:c2 + 1]
                    if np.sum(submatrix) == 93:
                        res.append(submatrix)
    return res