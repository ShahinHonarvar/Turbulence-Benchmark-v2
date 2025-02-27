def submatrix_with_particular_sum(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix[0])):
                    value = sum([row[p] for row in matrix[i:k + 1] for p in range(j, l + 1)])
                    if value == -863:
                        final_matrix = [[row[p] for p in range(j, l + 1)] for row in matrix[i:k + 1]]
                        return final_matrix
    return []