def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    submatrix_count = 0
    for i in range(rows):
        for j in range(cols):
            if rows - i >= n and cols - j >= n:
                submatrix = matrix[i:i + n, j:j + n]
                if np.sum(submatrix == 85) == n * n:
                    submatrix_count += 1
    return submatrix_count