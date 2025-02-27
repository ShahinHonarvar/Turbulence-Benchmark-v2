def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    second_largest = float('-inf')
    largest = float('-inf')
    for num in nums[:2]:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    if second_largest == float('-inf'):
        return None
    return second_largest