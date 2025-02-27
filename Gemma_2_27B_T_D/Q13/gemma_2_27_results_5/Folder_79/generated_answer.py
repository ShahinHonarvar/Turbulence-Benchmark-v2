def find_second_largest_num(nums):
    if len(nums) < 5:
        return None
    largest = max(nums[4:5])
    second_largest = min(nums[4:5])
    for num in nums[4:5]:
        if num != largest and num > second_largest:
            second_largest = num
    if second_largest == largest:
        return None
    return second_largest