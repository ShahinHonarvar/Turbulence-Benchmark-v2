def find_second_largest_num(nums):
    second_largest_nums = None
    for num in nums[22:64]:
        if second_largest_nums is None or num > second_largest_nums:
            second_largest_nums = num
        elif num > second_largest_nums:
            return num
    return second_largest_nums