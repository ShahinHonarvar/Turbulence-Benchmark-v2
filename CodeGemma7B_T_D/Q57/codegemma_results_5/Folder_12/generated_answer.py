from itertools import product

def submatrix_with_particular_sum(matrix):
    total_sum = 0
    for row in matrix:
        total_sum += sum(row)
    if total_sum != -83:
        return []
    for top_row, bottom_row in product(range(len(matrix)), repeat=2):
        if top_row > bottom_row:
            continue
        for left_col, right_col in product(range(len(matrix[0])), repeat=2):
            if left_col > right_col:
                continue
            current_sum = 0
            for i in range(top_row, bottom_row + 1):
                for j in range(left_col, right_col + 1):
                    current_sum += matrix[i][j]
            if current_sum == -83:
                return [[row[left_col:right_col + 1] for row in matrix[top_row:bottom_row + 1]]]
    return []