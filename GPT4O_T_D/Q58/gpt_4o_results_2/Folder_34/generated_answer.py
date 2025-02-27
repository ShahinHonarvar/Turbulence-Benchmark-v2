import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for r in range(rows):
        for c in range(cols):
            for r_end in range(r, rows):
                for c_end in range(c, cols):
                    num_elements = (r_end - r + 1) * (c_end - c + 1)
                    if num_elements == 83:
                        count += 1
                    elif num_elements > 83:
                        break
    return count