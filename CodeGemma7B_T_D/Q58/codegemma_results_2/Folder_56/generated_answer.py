from numpy import*

def submatrix_with_n_numbers(matrix):
    return sum(((matrix[i:i + x, :-x + y] == 68).sum() == x * y for x in range(1, matrix.shape[0] + 1) for y in range(1, matrix.shape[1] + 1) for i in range(matrix.shape[0] + 1 - x)))