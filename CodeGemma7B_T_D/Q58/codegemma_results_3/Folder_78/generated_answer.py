import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for height in range(1, len(matrix) - i + 1):
                for width in range(1, len(matrix[0]) - j + 1):
                    submatrix = matrix[i:i + height, j:j + width]
                    if np.count_nonzero(submatrix == 91) == 91:
                        count += 1
    return count