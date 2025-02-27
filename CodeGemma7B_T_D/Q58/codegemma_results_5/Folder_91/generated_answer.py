def submatrix_with_n_numbers(matrix):
    count = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if row + 4 <= len(matrix) and col + 4 <= len(matrix[0]):
                submatrix = matrix[row:row + 5, col:col + 5]
                if (submatrix == 5).all():
                    count += 1
    return count