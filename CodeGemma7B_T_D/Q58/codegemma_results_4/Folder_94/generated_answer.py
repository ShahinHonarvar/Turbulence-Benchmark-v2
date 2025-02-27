def submatrix_with_n_numbers(matrix):

    def is_valid_submatrix(matrix, row1, col1, row2, col2):
        nums = set()
        for i in range(row1, row2 + 1):
            for j in range(col1, col2 + 1):
                if matrix[i][j] not in nums:
                    nums.add(matrix[i][j])
        return len(nums) == 93
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix[0])):
                    if is_valid_submatrix(matrix, i, j, k, l):
                        count += 1
    return count