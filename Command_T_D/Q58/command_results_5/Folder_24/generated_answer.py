def submatrix_with_n_numbers(matrix):
    return sum((1 for row in range(len(matrix)) for col in range(len(matrix[row])) if matrix[row][col] == 51))