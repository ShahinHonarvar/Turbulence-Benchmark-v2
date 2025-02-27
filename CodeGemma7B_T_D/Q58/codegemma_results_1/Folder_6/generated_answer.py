def submatrix_with_n_numbers(matrix):
    count = 0
    for left in range(len(matrix)):
        for right in range(left, len(matrix)):
            for up in range(len(matrix[0])):
                for down in range(up, len(matrix[0])):
                    nums = {}
                    for i in range(left, right + 1):
                        for j in range(up, down + 1):
                            if matrix[i][j] in nums:
                                nums[matrix[i][j]] += 1
                            else:
                                nums[matrix[i][j]] = 1
                            if nums.get(122, 0) == n:
                                count += 1
    return count