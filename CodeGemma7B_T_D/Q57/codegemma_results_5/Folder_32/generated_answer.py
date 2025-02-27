from itertools import combinations
        import numpy as np

def submatrix_with_particular_sum(matrix):
    res = []
    s = sum(matrix.flatten())
    combinations_of_two_values = combinations(range(len(matrix)), 2)
    combinations_of_three_values = combinations(range(len(matrix)), 3)
    for row_start, row_finish in combinations_of_two_values:
        for col_start, col_finish in combinations_of_two_values:
            a = matrix[row_start:row_finish, col_start:col_finish]
            if a.sum() == s - 901:
                res.append((row_start, row_finish, col_start, col_finish))
    for col in combinations_of_three_values:
        for row in combinations_of_three_values:
            a = matrix[min(row):max(row) + 1, min(col):max(col) + 1]
            if a.sum() == s - 901:
                res.append((min(row), max(row), min(col), max(col)))
    return res