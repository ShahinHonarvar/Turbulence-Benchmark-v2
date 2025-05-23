def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    subset = nums[0:4]
    if len(subset) < 2:
        return None
    largest = max(subset)
    second_largest = None
    for num in subset:
        if num != largest and (second_largest is None or num > second_largest):
            second_largest = num
    return second_largest