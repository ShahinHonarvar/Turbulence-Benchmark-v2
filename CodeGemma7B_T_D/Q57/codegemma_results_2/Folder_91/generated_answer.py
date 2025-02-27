def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []
    for i in range(rows):
        for j in range(i + 1, rows):
            for k in range(cols):
                for l in range(k + 1, cols):
                    submatrix = matrix[i:j + 1][:, k:l + 1]
                    if submatrix.sum() == -6:
                        result.append(list(submatrix.flatten()))
    return result