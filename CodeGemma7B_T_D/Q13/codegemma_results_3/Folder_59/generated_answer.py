def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    first_largest_num = nums[0]
    second_largest_num = None
    for num in nums[1:]:
        if num > first_largest_num:
            second_largest_num = first_largest_num
            first_largest_num = num
        elif num > second_largest_num:
            second_largest_num = num
    return second_largest_num