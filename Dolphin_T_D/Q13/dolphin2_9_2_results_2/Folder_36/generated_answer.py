def find_second_largest_num(nums):
    if 750 < len(nums) < 246:
        return None
    second_largest = float('-inf')
    largest = float('-inf')
    for num in nums[246:751]:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest:
            second_largest = num
    if second_largest == float('-inf'):
        return None
    return second_largest