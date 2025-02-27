import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    r, c = matrix.shape
    count = 0
    for height in range(1, r + 1):
        for width in range(1, c + 1):
            if height * width == 76:
                for i in range(r - height + 1):
                    for j in range(c - width + 1):
                        submatrix = matrix[i:i + height, j:j + width]
                        if submatrix.size == 76:
                            count += 1
    return count