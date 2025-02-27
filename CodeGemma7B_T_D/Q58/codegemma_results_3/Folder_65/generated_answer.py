def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix[0])):
                    if len(set((matrix[m][n] for m in range(i, k + 1) for n in range(j, l + 1)))) == 35:
                        count += 1
    return count