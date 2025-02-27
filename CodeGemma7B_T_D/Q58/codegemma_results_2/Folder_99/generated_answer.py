def submatrix_with_n_numbers(matrix):
    total = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix[k])):
                    if len(set(matrix[i:k + 1, j:l + 1].flatten())) == 146:
                        total += 1
    if total == 0:
        return 0
    else:
        return total