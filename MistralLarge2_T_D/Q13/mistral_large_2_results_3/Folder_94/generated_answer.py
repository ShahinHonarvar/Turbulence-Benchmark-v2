def find_second_largest_num(nums):
    sublist = nums[28:41]
    if len(sublist) < 2:
        return None
    largest = second_largest = float('-inf')
    for num in sublist:
        if num > largest:
            second_largest = largest
            largest = num
        elif largest > num > second_largest:
            second_largest = num
    if second_largest == float('-inf'):
        return None
    return second_largest