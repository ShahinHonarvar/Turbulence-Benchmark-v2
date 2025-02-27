def submatrix_with_particular_sum(matrix_input):
    output_list = []
    for i in range(len(matrix_input)):
        for j in range(len(matrix_input[i])):
            for k in range(i + 1, len(matrix_input)):
                for l in range(j + 1, len(matrix_input[k])):
                    temp_sum = 0
                    for m in range(i, k + 1):
                        for n in range(j, l + 1):
                            temp_sum += matrix_input[m][n]
                    if temp_sum == -15:
                        output_list.append([[i, j], [k, l]])
    return output_list