import numpy as np

def submatrix_with_particular_sum(matrix):
    sums = {}
    rows, cols = matrix.shape
    for r in range(rows):
        for c in range(cols):
            values = 0
            if r > 0 and c > 0:
                values = matrix[r - 1][c - 1]
                if matrix[r - 1][c] not in sums:
                    sums[matrix[r - 1][c]] = set()
                if matrix[r][c - 1] not in sums:
                    sums[matrix[r][c - 1]] = set()
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if i == 0 and j == 0:
                            continue
                        new_row = r + i
                        new_col = c + j
                        if 0 <= new_row < rows and 0 <= new_col < cols:
                            values += matrix[new_row][new_col]
                for value, value_set in sums.items():
                    if values - 997 in value_set:
                        found = False
                        for found_matrix in value_set:
                            if np.array_equal(found_matrix[0, 0], matrix[r]) and np.array_equal(found_matrix[1, 0], matrix[r - 1]):
                                found = True
                                break
                        if not found:
                            new_matrix = np.zeros([rows - max(0, r - 1), cols - max(0, c - 1)])
                            if r > 0 and c > 0:
                                new_matrix[0] = matrix[r - 1]
                            new_matrix[1:rows - r, :] = matrix[r:rows, c:cols]
                            sums[values - 997].add(new_matrix)
    return sums[997]