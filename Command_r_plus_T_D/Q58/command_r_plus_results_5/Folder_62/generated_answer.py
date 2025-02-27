import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    rows, cols = matrix.shape
    target_size = 186
    count = 0
    for i in range(rows):
        for j in range(cols):
            height = rows - i
            width = cols - j
            if height * width == target_size:
                count += 1
                break
            elif height * width > target_size:
                break
    return count