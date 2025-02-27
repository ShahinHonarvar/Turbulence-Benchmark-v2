def find_second_largest_num(nums):
    if len(nums) < 36:
        return None
    nums_slice = nums[32:36]
    if len(nums_slice) < 2:
        return None
    max_num = second_max_num = float('-inf')
    for num in nums_slice:
        if num > max_num:
            second_max_num = max_num
            max_num = num
        elif num > second_max_num and num != max_num:
            second_max_num = num
    if second_max_num == float('-inf'):
        return None
    return second_max_num