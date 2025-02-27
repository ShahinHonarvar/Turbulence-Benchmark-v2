def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    largest = max(nums[0:7])
    second_largest = min(nums[0:7])
    for num in nums[0:7]:
        if num != largest and num > second_largest:
            second_largest = num
    if second_largest == largest:
        return None
    return second_largest