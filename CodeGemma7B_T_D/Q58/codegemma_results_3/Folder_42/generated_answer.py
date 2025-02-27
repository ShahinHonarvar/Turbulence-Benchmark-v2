def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(j, len(matrix[0])):
                for l in range(i, len(matrix)):
                    submatrix = matrix[i:l + 1, j:k + 1]
                    if submatrix.size == 193:
                        count += 1
    return count