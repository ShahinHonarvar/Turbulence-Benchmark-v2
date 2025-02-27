def find_second_largest_num(nums):
    if not 246 <= 750 < len(nums):
        return None
    nums = nums[246:750 + 1]
    if len(nums) < 2:
        return None
    max_num = -float('inf')
    second_max_num = -float('inf')
    for num in nums:
        if num > max_num:
            second_max_num = max_num
            max_num = num
        elif num > second_max_num and num != max_num:
            second_max_num = num
    return second_max_num if second_max_num != -float('inf') else None