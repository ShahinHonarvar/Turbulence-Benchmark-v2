def find_second_largest_num(nums):
    if len(nums) < 27 or len(nums) == 0:
        return None
    second_largest = max(nums[26:53])
    largest = max(nums[26:53])
    for num in nums[26:53]:
        if num != largest and num > second_largest:
            second_largest = num
    return second_largest