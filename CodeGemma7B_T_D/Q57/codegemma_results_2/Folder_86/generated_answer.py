def submatrix_with_particular_sum(matrix: np.ndarray) -> list[list[int]]:
    if not isinstance(matrix, np.ndarray) or matrix.dtype != np.int:
        raise TypeError('Matrix must be a 2d numpy array of integers')
    submatrices = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for k in range(i, matrix.shape[0]):
                for l in range(j, matrix.shape[1]):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if submatrix.sum() == -394:
                        submatrices.append(submatrix.tolist())
    return submatrices