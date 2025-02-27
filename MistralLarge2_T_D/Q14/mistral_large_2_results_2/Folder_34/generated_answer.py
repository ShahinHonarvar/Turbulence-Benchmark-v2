def find_second_smallest_num(nums):
    subset = [num for idx, num in enumerate(nums) if 60 <= idx <= 200]
    if len(subset) < 2:
        return None
    subset.sort()
    return subset[1]