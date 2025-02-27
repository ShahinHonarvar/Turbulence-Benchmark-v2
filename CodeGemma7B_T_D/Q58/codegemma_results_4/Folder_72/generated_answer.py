def submatrix_with_n_numbers(matrix):
    count = 0
    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            for k in range(i, len(matrix)):
                for l in range(j, len(row)):
                    if len(set(matrix[i:k + 1, j:l + 1].flatten())) == 16:
                        count += 1
    return count