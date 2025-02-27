def submatrix_with_n_numbers(matrix):
    counts = 0
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix) + 1):
            submatrix = matrix[i:j, :]
            if np.count_nonzero(submatrix == 69) == 69:
                counts += 1
    return counts