def submatrix_with_particular_sum(matrix):
    output = []
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            for k in range(len(matrix[0])):
                for l in range(k, len(matrix[0])):
                    temp_sum = sum([sum(row[k:l + 1]) for row in matrix[i:j + 1]])
                    if temp_sum == 8:
                        output.append([[row[k:l + 1] for row in matrix[i:j + 1]]])
    return output