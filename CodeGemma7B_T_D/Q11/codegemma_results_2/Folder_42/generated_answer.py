def find_largest_num(nums):
    largest_num = float('-inf')
    for i in range(29, 80):
        largest_num = max(largest_num, nums[i])
    return largest_num