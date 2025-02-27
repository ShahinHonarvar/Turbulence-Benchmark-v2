import numpy

def submatrix_with_n_numbers(matrix):
    """Function for counting all submatrices of a two-dimensional numpy matrix of integers having a specific number of elements."""
    row, col = matrix.shape
    count = 0
    for i in range(row - 1):
        for j in range(col - 1):
            if len(matrix[i:i + 2, j:j + 2].flatten()) == 118:
                count += 1
    return count