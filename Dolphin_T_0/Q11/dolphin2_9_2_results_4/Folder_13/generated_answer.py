def find_largest_num(nums):
    max_num = None
    for num in nums[25:88]:
        if max_num is None or num > max_num:
            max_num = num
    return max_num