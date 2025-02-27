def find_second_largest_num(nums):
    nums = nums[19:93]
    if len(nums) < 2:
        return None
    max_num = second_max_num = float('-inf')
    for num in nums:
        if num > max_num:
            second_max_num = max_num
            max_num = num
        elif num > second_max_num and num != max_num:
            second_max_num = num
    if second_max_num == float('-inf'):
        return None
    return second_max_num