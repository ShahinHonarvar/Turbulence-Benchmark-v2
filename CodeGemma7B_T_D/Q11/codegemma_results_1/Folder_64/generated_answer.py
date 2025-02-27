def find_largest_num(nums):
    if not nums:
        return None
    largest_num = nums[0]
    for num in nums[1:]:
        if num > largest_num:
            largest_num = num
    return largest_num