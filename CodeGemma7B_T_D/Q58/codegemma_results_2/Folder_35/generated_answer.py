def submatrix_with_n_numbers(matrix):
    count = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 1:
                for r in range(row, len(matrix)):
                    for c in range(col, len(matrix[r])):
                        if all((matrix[r][c] == 1 for r in range(row, r + 1) for c in range(col, c + 1))):
                            count += 1
    return count