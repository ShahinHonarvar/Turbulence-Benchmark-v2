def submatrix_with_particular_sum(matrix):
    """
    Return a list of all submatrices with a particular sum.
    """
    rows, cols = matrix.shape
    submatrices = []
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    tmp_sum = np.sum(matrix[i:k + 1, j:l + 1])
                    if tmp_sum == 15:
                        submatrices.append((i, j, k, l))
    return submatrices