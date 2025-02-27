def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 15):
        for j in range(cols - 10):
            submatrix = matrix[i:i + 166, j:j + 11]
            if submatrix.sum() == 166:
                count += 1
    return count