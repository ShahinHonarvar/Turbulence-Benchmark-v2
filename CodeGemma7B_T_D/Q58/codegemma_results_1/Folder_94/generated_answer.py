def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            for k in range(len(matrix[0])):
                for l in range(k + 1, len(matrix[0])):
                    temp = matrix[i:j + 1, k:l + 1]
                    if (temp == 93).sum() == 93:
                        count += 1
    return count