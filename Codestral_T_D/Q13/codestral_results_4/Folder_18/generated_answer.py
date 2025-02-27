def find_second_largest_num(nums):
    sublist = nums[35:50]
    if len(sublist) < 2:
        return None
    largest = second_largest = float('-inf')
    for num in sublist:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num < largest:
            second_largest = num
    if second_largest == float('-inf'):
        return None
    return second_largest