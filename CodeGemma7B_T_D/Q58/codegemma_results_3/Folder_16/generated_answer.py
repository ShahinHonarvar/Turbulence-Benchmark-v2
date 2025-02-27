import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for left in range(len(matrix)):
        for right in range(left, len(matrix)):
            for top in range(len(matrix)):
                for down in range(top, len(matrix)):
                    submatrix = matrix[left:right + 1, top:down + 1]
                    if np.count_nonzero(submatrix == 154) == 154:
                        count += 1
    return count