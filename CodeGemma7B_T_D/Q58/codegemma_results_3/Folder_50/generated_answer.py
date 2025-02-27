def submatrix_with_n_numbers(matrix):
    """
    Counts the number of submatrices of the given matrix that contain 40 integers each.
    """
    count = 0
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            for k in range(j + 1, len(matrix)):
                for l in range(k + 1, len(matrix)):
                    submatrix = matrix[i:j + 1, k:l + 1]
                    if submatrix.size == 40:
                        count += 1
    return count