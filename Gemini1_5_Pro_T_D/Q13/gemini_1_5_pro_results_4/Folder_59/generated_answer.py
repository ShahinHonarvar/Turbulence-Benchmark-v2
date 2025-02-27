def find_second_largest_num(nums):
    if len(nums) < 2 or len(nums) > 10:
        return None
    largest = max(nums[0:10])
    second_largest = min(nums[0:10])
    for i in range(min(10, len(nums))):
        if nums[i] != largest and nums[i] > second_largest:
            second_largest = nums[i]
    return second_largest