def find_second_largest_num(nums):
    if len(nums) < 86:
        return None
    subarray = nums[75:86]
    if len(subarray) < 2:
        return None
    first = second = float('-inf')
    for num in subarray:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    return second if second != float('-inf') else None