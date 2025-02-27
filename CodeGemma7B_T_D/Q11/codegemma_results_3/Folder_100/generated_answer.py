def find_largest_num(nums):
    largest_num = float('-inf')
    for i in range(42, 69):
        if nums[i] > largest_num:
            largest_num = nums[i]
    return largest_num