def find_second_largest_num(nums):
    sublist = nums[23:24]
    if len(sublist) < 2:
        return None
    first_largest = second_largest = float('-inf')
    for num in sublist:
        if num > first_largest:
            second_largest = first_largest
            first_largest = num
        elif num > second_largest and num < first_largest:
            second_largest = num
    if second_largest == float('-inf'):
        return None
    return second_largest