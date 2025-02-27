def submatrix_with_particular_sum(matrix):
    result = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(i + 1, len(matrix)):
                for l in range(j + 1, len(matrix[0])):
                    new_matrix = matrix[i:k + 1]
                    for row in new_matrix:
                        row = row[j:l + 1]
                    sum_of_matrix = sum([sum(row) for row in new_matrix])
                    if sum_of_matrix == -83:
                        result.append(new_matrix)
    return result