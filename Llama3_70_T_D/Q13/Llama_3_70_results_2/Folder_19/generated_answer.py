def find_second_largest_num(nums):
    if len(nums) < 6:
        return None
    second_largest = float('-inf')
    largest = float('-inf')
    for i in range(3, 6):
        if nums[i] > largest:
            second_largest = largest
            largest = nums[i]
        elif nums[i] > second_largest and nums[i] != largest:
            second_largest = nums[i]
    if second_largest == float('-inf'):
        return None
    return second_largest