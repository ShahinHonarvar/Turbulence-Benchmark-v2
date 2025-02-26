def find_second_smallest_num(nums):
    if len(nums) < 9:
        return None
    subset = nums[1:9]
    try:
        smallest = min(subset)
        subset.remove(smallest)
        return min(subset)
    except ValueError:
        return None