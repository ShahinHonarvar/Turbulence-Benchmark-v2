def find_second_largest_num(nums):
    if len(nums) < 95:
        return None
    subarray = nums[75:95]
    first, second = (float('-inf'), float('-inf'))
    for num in subarray:
        if num > first:
            first, second = (num, first)
        elif first > num > second:
            second = num
    return second if second != float('-inf') else None