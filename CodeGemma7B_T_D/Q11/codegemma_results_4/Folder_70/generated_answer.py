def find_largest_num(nums):
    largest_num = float('-inf')
    for num in nums[28:33]:
        if num > largest_num:
            largest_num = num
    return largest_num