def submatrix_with_particular_sum(matrix):
    dimensions = (len(matrix), len(matrix[0]))
    all_submatrices = []
    for row_start in range(dimensions[0]):
        for row_end in range(row_start, dimensions[0]):
            for col_start in range(dimensions[1]):
                for col_end in range(col_start, dimensions[1]):
                    total_sum = 0
                    for row in range(row_start, row_end + 1):
                        for col in range(col_start, col_end + 1):
                            total_sum += matrix[row][col]
                    if total_sum == 416:
                        all_submatrices.append((row_start, row_end + 1, col_start, col_end + 1))
    return all_submatrices