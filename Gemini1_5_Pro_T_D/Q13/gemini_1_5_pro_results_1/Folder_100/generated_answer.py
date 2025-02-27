def find_second_largest_num(nums):
    if len(nums) < 69:
        return None
    sub_nums = nums[42:69]
    if len(set(sub_nums)) < 2:
        return None
    largest_num = max(sub_nums)
    second_largest_num = min(sub_nums)
    for num in sub_nums:
        if second_largest_num < num < largest_num:
            second_largest_num = num
    return second_largest_num