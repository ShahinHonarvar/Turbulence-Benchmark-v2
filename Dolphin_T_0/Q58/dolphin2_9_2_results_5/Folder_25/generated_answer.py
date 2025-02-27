import numpy as np

def submatrix_with_n_numbers(matrix):
    queue = []
    row_count, column_count = matrix.shape
    for row in range(row_count):
        for column in range(column_count):
            if matrix[row][column] == 66:
                new_matrix = matrix[row:row + 2, column:column + 2]
                if new_matrix.size == 9:
                    queue.append(new_matrix)
    return len(queue)