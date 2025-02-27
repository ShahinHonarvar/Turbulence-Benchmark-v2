def find_second_largest_num(nums):
    if len(nums) <= 88:
        sublist = nums[22:89]
    else:
        sublist = nums[22:88]
    if len(sublist) < 2:
        return None
    first_largest = second_largest = float('-inf')
    for num in sublist:
        if num > first_largest:
            second_largest = first_largest
            first_largest = num
        elif num > second_largest:
            second_largest = num
    if second_largest == float('-inf'):
        return None
    return second_largest