def find_second_largest_num(nums):
    if len(nums) <= 30 or len(nums) < 20:
        return None
    elif len(nums) > 30:
        nums = nums[20:31]
    else:
        nums = nums[20:]
    max_num = nums[0]
    second_max_num = None
    for num in nums:
        if num > max_num:
            second_max_num = max_num
            max_num = num
        elif num != max_num and second_max_num is None or num > second_max_num:
            second_max_num = num
    return second_max_num