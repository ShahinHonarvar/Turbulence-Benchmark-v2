def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix[0])):
                    temp_matrix = matrix[i:k + 1, j:l + 1]
                    if len(temp_matrix) != len(set(temp_matrix.reshape(1, -1)[0])):
                        continue
                    count += 1
    return count