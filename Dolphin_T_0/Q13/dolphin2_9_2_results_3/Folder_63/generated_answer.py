def find_second_largest_num(nums):
    second_largest_num = None
    for num in nums[22:89]:
        if second_largest_num is None or num > second_largest_num:
            second_largest_num = num
    return second_largest_num