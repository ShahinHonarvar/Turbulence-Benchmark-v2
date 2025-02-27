import numpy

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            submatrix = matrix[i:i + 54, j:j + 54]
            if submatrix.size == 54 and submatrix.sum() == 54 * 55:
                count += 1
    return count