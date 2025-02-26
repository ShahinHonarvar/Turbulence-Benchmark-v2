def find_second_largest_num(nums):
    if len(nums) <= 209:
        return None
    subset = nums[209:557]
    if len(subset) <= 1:
        return None
    largest = max(subset)
    second_largest = max((num for num in subset if num != largest))
    return second_largest