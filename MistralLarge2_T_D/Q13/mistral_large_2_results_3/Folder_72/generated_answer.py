def find_second_largest_num(nums):
    if len(nums) < 52:
        return None
    sublist = nums[29:52]
    if len(sublist) < 2:
        return None
    first_largest = max(sublist)
    second_largest = float('-inf')
    for num in sublist:
        if num != first_largest:
            second_largest = max(second_largest, num)
    if second_largest == float('-inf'):
        return None
    return second_largest