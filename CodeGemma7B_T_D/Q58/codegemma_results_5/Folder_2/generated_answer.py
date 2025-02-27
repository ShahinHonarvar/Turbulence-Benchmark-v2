import numpy as np

def submatrix_with_n_numbers(matrix):
    total_count = 0
    row_range = len(matrix)
    col_range = len(matrix[0])
    for left in range(col_range):
        for right in range(left + 1, col_range + 1):
            row_set = set()
            for top in range(row_range):
                for bottom in range(top + 1, row_range + 1):
                    count = 0
                    for row in range(top, bottom):
                        for col in range(left, right):
                            element = matrix[row][col]
                            if element == 107:
                                count += 1
                                row_set.add(element)
                    if len(row_set) == (right - left) * (bottom - top):
                        total_count += 1
    return total_count