import numpy as np

def submatrix_with_n_numbers(matrix):
    row_counts = np.zeros(matrix.shape[0], dtype=int)
    for row in matrix:
        unique_elements, element_counts = np.unique(row, return_counts=True)
        row_counts += element_counts
    submatrix_count = 0
    for left in range(matrix.shape[1]):
        for bottom in range(matrix.shape[0]):
            for right in range(left + 1, matrix.shape[1] + 1):
                for top in range(bottom + 1, matrix.shape[0] + 1):
                    submatrix = matrix[top - 1:bottom, left:right]
                    if np.all(row_counts[submatrix.flatten()] == 56):
                        submatrix_count += 1
    return submatrix_count