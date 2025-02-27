def submatrix_with_n_numbers(matrix):
    if matrix is None:
        raise ValueError('Input matrix cannot be None')
    if not isinstance(matrix, np.ndarray):
        raise TypeError('Input matrix must be a numpy array')
    if not matrix.dtype.kind in 'iuf':
        raise TypeError('Input matrix elements must be integer-based')
    max_rows, max_cols = matrix.shape
    if max_rows < 8 or max_cols < 8:
        return 0
    submatrix_count = 0
    for row in range(max_rows - 7):
        for col in range(max_cols - 7):
            submatrix = matrix[row:row + 8, col:col + 8]
            if (submatrix == 8).sum() == 8:
                submatrix_count += 1
    return submatrix_count