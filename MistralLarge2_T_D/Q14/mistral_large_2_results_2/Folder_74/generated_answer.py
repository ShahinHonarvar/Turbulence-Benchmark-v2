def find_second_smallest_num(nums):
    subset = nums[36:47]
    if len(subset) < 2:
        return None
    first_smallest = min(subset)
    subset.remove(first_smallest)
    second_smallest = min(subset)
    return second_smallest