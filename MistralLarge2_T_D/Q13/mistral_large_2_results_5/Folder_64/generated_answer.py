def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    first_largest = float('-inf')
    second_largest = float('-inf')
    for i in range(5):
        if nums[i] > first_largest:
            second_largest = first_largest
            first_largest = nums[i]
        elif first_largest > nums[i] > second_largest:
            second_largest = nums[i]
    if second_largest == float('-inf'):
        return None
    return second_largest