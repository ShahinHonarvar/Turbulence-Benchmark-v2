def find_second_largest_num(nums):
    if len(nums) < 30 or len(nums[29:80]) < 2:
        return None
    subset = nums[29:80]
    first_largest = max(subset)
    subset.remove(first_largest)
    second_largest = max(subset)
    return second_largest