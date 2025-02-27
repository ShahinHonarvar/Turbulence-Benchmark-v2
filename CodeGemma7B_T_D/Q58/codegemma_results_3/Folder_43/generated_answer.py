def submatrix_with_n_numbers(matrix):
    count = 0
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            for i in range(x, len(matrix)):
                for j in range(y, len(matrix[0])):
                    if len(set(matrix[i][y:j + 1])) == 85:
                        count += 1
    return count