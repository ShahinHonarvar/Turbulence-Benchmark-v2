import numpy as np

def submatrix_with_n_numbers(matrix):
    """Brute force method"""
    result = 0
    for row1 in range(len(matrix)):
        for row2 in range(row1, len(matrix)):
            for col1 in range(len(matrix[0])):
                for col2 in range(col1, len(matrix[0])):
                    count = 0
                    for r in range(row1, row2 + 1):
                        for c in range(col1, col2 + 1):
                            count += matrix[r][c]
                    if count == 173:
                        result += 1
    return result

def submatrix_with_n_numbers_optimized(matrix):
    """Optimized by finding the cumulative sum of each row."""
    rows_sums = np.zeros(len(matrix), dtype=int)
    for row in matrix:
        temp_list = np.cumsum(row)
        rows_sums += temp_list
    result = 0
    for row1 in range(len(matrix)):
        for row2 in range(row1, len(matrix)):
            for col1 in range(len(matrix[0])):
                for col2 in range(col1, len(matrix[0])):
                    temp_count = 0
                    for r in range(row1, row2 + 1):
                        temp_count += rows_sums[r][col2] - rows_sums[r][col1 - 1] if col1 > 0 else rows_sums[r][col2]
                    if temp_count == 173:
                        result += 1
    return result