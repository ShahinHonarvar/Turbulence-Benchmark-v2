import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    target_count = 53
    count = 0
    for row in range(rows):
        for col in range(cols):
            submatrix = []
            for r in range(row, rows):
                submatrix.append(matrix[r][col:])
                flat_list = [item for sublist in submatrix for item in sublist]
                if len(flat_list) == target_count:
                    count += 1
                if len(flat_list) > target_count:
                    break
    for col in range(cols):
        for row in range(rows):
            submatrix = []
            for c in range(col, cols):
                submatrix.append(matrix[row:, c])
                flat_list = [item for sublist in submatrix for item in sublist]
                if len(flat_list) == target_count:
                    count += 1
                if len(flat_list) > target_count:
                    break
    return count