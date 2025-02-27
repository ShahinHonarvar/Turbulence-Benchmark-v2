def submatrix_with_n_numbers(matrix):
    flattened_matrix = matrix.flatten()
    submatrix_count = 0
    for i in range(len(flattened_matrix)):
        for j in range(i + 1, len(flattened_matrix)):
            submatrix = flattened_matrix[i:j + 1]
            if len(submatrix) == 28 and submatrix.sum() == 700:
                submatrix_count += 1
    return submatrix_count