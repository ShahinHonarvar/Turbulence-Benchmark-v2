import numpy as np

def submatrix_with_n_numbers(matrix):
    length = len(matrix[0])
    width = len(matrix)
    numbers = 38
    count = 0
    for h in range(1, length, numbers):
        for w in range(1, width, numbers):
            submatrix = matrix[w - 1:w + numbers, h - 1:h + numbers]
            if np.count_nonzero(submatrix) == numbers:
                count += 1
    return count