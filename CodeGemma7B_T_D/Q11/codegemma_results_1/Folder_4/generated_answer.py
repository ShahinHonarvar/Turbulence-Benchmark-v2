def find_largest_num(nums):
    largest_num = float('-inf')
    for num in nums[12:93]:
        if num > largest_num:
            largest_num = num
    return largest_num