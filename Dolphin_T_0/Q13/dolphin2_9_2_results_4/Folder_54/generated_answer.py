def find_second_largest_num(nums):
    if not nums:
        return None
    second_max = float('-inf')
    max_val = float('-inf')
    for i in range(34, 56):
        if nums[i] > max_val:
            max_val, second_max = (nums[i], max_val)
        elif nums[i] > second_max and nums[i] != max_val:
            second_max = nums[i]
    if second_max == float('-inf'):
        return None
    return second_max