def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    first_largest = float('-inf')
    second_largest = float('-inf')
    for num in nums:
        if num > first_largest:
            second_largest = first_largest
            first_largest = num
        elif num > second_largest and num != first_largest:
            second_largest = num
    if second_largest == float('-inf'):
        return None
    return second_largest