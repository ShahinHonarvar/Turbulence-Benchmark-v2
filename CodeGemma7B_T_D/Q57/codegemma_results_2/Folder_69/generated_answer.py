def submatrix_with_particular_sum(matrix):
    sum_2 = 0
    sub_matrix = []
    maximum_sum = float('-inf')
    for i in range(len(matrix)):
        sum_1 = 0
        for j in range(len(matrix)):
            sum_1 += matrix[i][j]
            if i > 0:
                sum_2 = sum_2 + matrix[i][j] - matrix[i - 1][j]
            if sum_2 == 752:
                if maximum_sum < sum_2:
                    maximum_sum = sum_2
                    sub_matrix = matrix[i - 3][j - 3:j + 1]
                    for i2 in range(i - 3, i + 1):
                        for j2 in range(j - 3, j + 1):
                            sub_matrix[i2 - (i - 3)][j2 - (j - 3)] = matrix[i2][j2]
            elif sum_2 > maximum_sum:
                maximum_sum = sum_2
                sub_matrix = matrix[i - 3][j - 3:j + 1]
                for i2 in range(i - 3, i + 1):
                    for j2 in range(j - 3, j + 1):
                        sub_matrix[i2 - (i - 3)][j2 - (j - 3)] = matrix[i2][j2]
    return sub_matrix