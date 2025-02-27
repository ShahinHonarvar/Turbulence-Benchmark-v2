import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    total_elements = rows * cols
    return total_elements / 104 if total_elements % 104 == 0 else 0