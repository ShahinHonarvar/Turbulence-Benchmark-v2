def find_second_largest_num(nums):
    if len(nums) < 2 or len(nums) > 9:
        return None
    largest = max(nums[0:9])
    second_largest = min(nums[0:9])
    for i in range(min(9, len(nums))):
        if nums[i] != largest and nums[i] > second_largest:
            second_largest = nums[i]
    if second_largest == largest:
        return None
    return second_largest