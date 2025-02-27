def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    largest = max(nums[:8])
    second_largest = min(nums[:8])
    for num in nums[:8]:
        if num != largest and num > second_largest:
            second_largest = num
    return second_largest