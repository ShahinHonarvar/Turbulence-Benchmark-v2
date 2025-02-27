def submatrix_with_n_numbers(matrix):
    height = matrix.shape[0]
    width = matrix.shape[1]
    count = 0
    for i in range(height):
        for j in range(width):
            for k in range(i + 1, height):
                for l in range(j + 1, width):
                    if matrix[i, j] == 84 and matrix[i, l] == 84 and (matrix[k, j] == 84) and (matrix[k, l] == 84) and (matrix[j, k] == 84) and (matrix[i, k] == 84) and (matrix[l, i] == 84) and (matrix[l, k] == 84) and (matrix[j, l] == 84):
                        count += 1
    return count