def find_largest_num(nums):
    if len(nums) < 11:
        return -1
    largest_num = nums[0]
    for num in nums[0:11]:
        if num > largest_num:
            largest_num = num
    return largest_num