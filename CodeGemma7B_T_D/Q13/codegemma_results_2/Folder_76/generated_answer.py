def find_second_largest_num(nums):
    if len(nums) < 2:
        return 'None'
    largest = float('-inf')
    for num in nums:
        if num > largest:
            largest = num
    second_largest = float('-inf')
    for num in nums:
        if num < largest and num > second_largest:
            second_largest = num
    if second_largest == float('-inf'):
        return 'None'
    return second_largest