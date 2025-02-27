def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for top in range(rows):
        for bottom in range(top, rows):
            for left in range(cols):
                for right in range(left, cols):
                    submatrix = matrix[top:bottom + 1, left:right + 1]
                    if submatrix.size == 76:
                        count += 1
    return count