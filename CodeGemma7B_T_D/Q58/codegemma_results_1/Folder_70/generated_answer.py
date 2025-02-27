def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            submatrix = []
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix[0])):
                    submatrix.append(matrix[k][l])
                    if len(submatrix) == 173:
                        count += 1
    return count