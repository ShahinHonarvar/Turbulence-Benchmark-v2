def find_largest_num(nums):
    max_num = nums[56]
    for num in nums[56:83]:
        if num > max_num:
            max_num = num
    return max_num