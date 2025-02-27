def submatrix_with_n_numbers(matrix):
    total_count = 0
    rows, cols = matrix.shape
    for top in range(rows):
        for bottom in range(top, rows):
            col_set = set()
            for left in range(cols):
                for right in range(left, cols):
                    element = matrix[bottom, right] and matrix[top, left] and matrix[bottom, left] and matrix[top, right]
                    if element in col_set:
                        continue
                    col_set.add(element)
                    if len(col_set) == 104:
                        total_count += 1
    return total_count