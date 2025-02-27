import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    target_count = 47
    for row in range(rows):
        for col in range(cols):
            curr_count = 0
            for r in range(row, rows):
                curr_count += cols - col
                if curr_count == target_count:
                    count += 1
                elif curr_count > target_count:
                    break
                for c in range(col + 1, cols):
                    curr_count += r - row + 1
                    if curr_count == target_count:
                        count += 1
                    elif curr_count > target_count:
                        break
    return count