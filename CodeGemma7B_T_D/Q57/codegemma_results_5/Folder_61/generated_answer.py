def submatrix_with_particular_sum(matrix):
    list_of_submatrices = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(1, len(matrix) + 1):
                for l in range(1, len(matrix[0]) + 1):
                    if sum((a.flatten() for a in matrix[i:i + k, j:j + l])) == 8:
                        list_of_submatrices.append(matrix[i:i + k, j:j + l].tolist())
    return list_of_submatrices