def find_second_largest_num(nums):
    if len(nums) <= 17:
        return None
    subset = nums[17:79]
    if len(subset) < 2:
        return None
    largest = max(subset)
    subset_without_largest = [x for x in subset if x != largest]
    if not subset_without_largest:
        return None
    return max(subset_without_largest)