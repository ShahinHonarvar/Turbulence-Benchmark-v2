def find_second_largest_num(nums):
    if len(nums) < 2 or len(nums) > 4:
        return None
    largest = max(nums[0:4])
    second_largest = min(nums[0:4])
    for i in range(0, 4):
        if nums[i] != largest and nums[i] > second_largest:
            second_largest = nums[i]
    if second_largest == largest:
        return None
    return second_largest