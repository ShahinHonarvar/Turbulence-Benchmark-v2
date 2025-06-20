def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for x in range(i, matrix.shape[0]):
                for y in range(j, matrix.shape[1]):
                    if (x - i + 1) * (y - j + 1) == 72:
                        submatrix = matrix[i:x + 1, j:y + 1]
                        if submatrix.sum() == 72:
                            count += 1
    return count