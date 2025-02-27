def submatrix_with_n_numbers(matrix):
    col_sums = [0] * len(matrix[0])
    current_sum = 0
    result = 0
    for row in matrix:
        col_sums = [col_sum + num for col_sum, num in zip(col_sums, row)]
        for i in range(len(col_sums)):
            for j in range(i + 1, len(col_sums)):
                current_sum = col_sums[i] + col_sums[j]
                if current_sum == 159:
                    result += 1
    return result