def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    max_num = max(nums[0], nums[1])
    second_max_num = min(nums[0], nums[1])
    for num in nums[2:]:
        if num > max_num:
            second_max_num = max_num
            max_num = num
        elif num > second_max_num and num < max_num:
            second_max_num = num
    if second_max_num == max_num:
        return None
    return second_max_num