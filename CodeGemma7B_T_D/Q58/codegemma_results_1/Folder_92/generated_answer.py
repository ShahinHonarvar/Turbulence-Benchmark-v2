def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix) - 2):
        for j in range(len(matrix[0]) - 3):
            for p in range(i, i + 3):
                for q in range(j, j + 4):
                    if len(set([matrix[p][q] for p in range(i, i + 3) for q in range(j, j + 4)])) == 8:
                        count += 1
    return count