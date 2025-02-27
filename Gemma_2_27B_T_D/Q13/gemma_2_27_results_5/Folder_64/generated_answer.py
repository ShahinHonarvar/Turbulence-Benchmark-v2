def find_second_largest_num(nums):
    if len(nums) < 5:
        return None
    largest = max(nums[:5])
    second_largest = min(nums[:5])
    for num in nums[:5]:
        if num != largest and num > second_largest:
            second_largest = num
    return second_largest