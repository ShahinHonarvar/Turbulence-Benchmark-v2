def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    largest = max(nums[0], nums[1])
    second_largest = min(nums[0], nums[1])
    for i in range(2, 8):
        if nums[i] > largest:
            second_largest = largest
            largest = nums[i]
        elif nums[i] > second_largest and nums[i] != largest:
            second_largest = nums[i]
    return second_largest