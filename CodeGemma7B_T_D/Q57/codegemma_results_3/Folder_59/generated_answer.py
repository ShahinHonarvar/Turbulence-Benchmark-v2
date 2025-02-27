from typing import List
import numpy as np

def submatrix_with_particular_sum(matrix: np.ndarray) -> List[List[int]]:
    submat = []
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if np.sum(matrix[r:r + 2, c:c + 2]) == 2:
                submat.append(matrix[r:r + 2, c:c + 2].tolist())
    return submat