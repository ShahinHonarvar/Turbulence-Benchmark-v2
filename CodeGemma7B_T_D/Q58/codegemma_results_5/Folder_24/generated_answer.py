def submatrix_with_n_numbers(matrix):
    count = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            for r in range(row, len(matrix)):
                for c in range(col, len(matrix[r])):
                    submatrix = matrix[row:r + 1, col:c + 1]
                    if len(submatrix) * len(submatrix[0]) == 51:
                        count += 1
    return count