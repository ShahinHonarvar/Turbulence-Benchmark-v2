def submatrix_with_n_numbers(matrix):
    output = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix[0])):
                    temp_matrix = matrix[i:k + 1, j:l + 1]
                    if temp_matrix.size == 80:
                        output += 1
    return output