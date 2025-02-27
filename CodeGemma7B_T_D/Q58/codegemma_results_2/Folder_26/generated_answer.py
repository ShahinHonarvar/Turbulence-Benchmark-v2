def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(1, len(matrix) - i + 1):
                for l in range(1, len(matrix[0]) - j + 1):
                    submatrix = matrix[i:i + k, j:j + l]
                    if (submatrix == 115).sum() == k * l:
                        count += 1
    return count