def submatrix_with_n_numbers(matrix):
    count = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            for r in range(row, len(matrix)):
                for c in range(col, len(matrix[0])):
                    submatrix = matrix[row:r + 1][col:c + 1]
                    if len(submatrix) != 19:
                        continue
                    if all((num == 1 for row in submatrix for num in row)):
                        count += 1
    return count