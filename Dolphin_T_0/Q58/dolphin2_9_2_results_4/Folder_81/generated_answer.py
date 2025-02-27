import numpy as np

def submatrix_with_n_numbers(matrix):
    num_elements = 97
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for r in range(rows):
        for c in range(cols):
            if r + num_elements <= rows and c + num_elements <= cols:
                if np.sum(matrix[r:r + num_elements, c:c + num_elements]) == num_elements:
                    count += 1
    return count