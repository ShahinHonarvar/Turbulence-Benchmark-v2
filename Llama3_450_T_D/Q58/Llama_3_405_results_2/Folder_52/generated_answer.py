import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    n = 147
    for row in range(rows):
        for col in range(cols):
            curr_row, curr_col = (row, col)
            curr_count = 0
            while curr_row < rows and curr_col < cols and (curr_count < n):
                curr_count += cols - curr_col
                if curr_count >= n:
                    break
                curr_row += 1
            if curr_count >= n:
                count += 1
    for row in range(rows):
        for col in range(cols):
            curr_row, curr_col = (row, col)
            curr_count = 0
            while curr_row < rows and curr_col < cols and (curr_count < n):
                curr_count += rows - curr_row
                if curr_count >= n:
                    break
                curr_col += 1
            if curr_count >= n:
                count += 1
    return count // 2