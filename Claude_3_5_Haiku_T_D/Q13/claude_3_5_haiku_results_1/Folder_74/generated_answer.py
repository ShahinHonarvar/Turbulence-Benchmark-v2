def find_second_largest_num(nums):
    if len(nums) < 79 or len(nums) == 0:
        return None
    subset = nums[17:79]
    if len(subset) < 2:
        return None
    largest = max(subset)
    subset_without_largest = [num for num in subset if num != largest]
    if not subset_without_largest:
        return None
    return max(subset_without_largest)