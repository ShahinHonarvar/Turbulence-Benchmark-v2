def submatrix_with_particular_sum(matrix):
    output_list = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for k in range(i + 1, matrix.shape[0]):
                for l in range(j + 1, matrix.shape[1]):
                    temp_sum = 0
                    for x in range(i, k + 1):
                        for y in range(j, l + 1):
                            temp_sum += matrix[x][y]
                            if temp_sum == -6:
                                output_list.append([matrix[x][y] for x in range(i, k + 1) for y in range(j, l + 1)])
    return output_list