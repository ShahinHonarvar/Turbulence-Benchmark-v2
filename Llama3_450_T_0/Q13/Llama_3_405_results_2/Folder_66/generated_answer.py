def find_second_largest_num(nums):
    if len(nums) < 55:
        return None
    nums_slice = nums[50:55]
    if len(nums_slice) < 2:
        return None
    max_num = second_max = float('-inf')
    for num in nums_slice:
        if num > max_num:
            second_max = max_num
            max_num = num
        elif num > second_max and num != max_num:
            second_max = num
    if second_max == float('-inf'):
        return None
    return second_max