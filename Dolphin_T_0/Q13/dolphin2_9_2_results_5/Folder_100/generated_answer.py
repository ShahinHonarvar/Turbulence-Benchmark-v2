def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    largest, second_largest = (float('-inf'), float('-inf'))
    for i in range(42, 69):
        if nums[i] > largest:
            second_largest = largest
            largest = nums[i]
        elif nums[i] > second_largest and nums[i] != largest:
            second_largest = nums[i]
    if second_largest == float('-inf'):
        return None
    return second_largest