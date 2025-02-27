def find_largest_num(nums):
    max_num = float('-inf')
    for i in range(75, 86):
        if nums[i] > max_num:
            max_num = nums[i]
    return max_num