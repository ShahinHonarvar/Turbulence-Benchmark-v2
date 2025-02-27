def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix[0])):
                    if len({matrix[p][q] for p in range(i, k + 1) for q in range(j, l + 1)}) == 5:
                        count += 1
    return count