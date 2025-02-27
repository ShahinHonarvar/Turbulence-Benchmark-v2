def find_second_largest_num(nums):
    if len(nums) < 775:
        return None
    segment = nums[667:775]
    if len(segment) < 2:
        return None
    first, second = (float('-inf'), float('-inf'))
    for num in segment:
        if num > first:
            first, second = (num, first)
        elif num > second:
            second = num
    return second if second != float('-inf') else None