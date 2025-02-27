def find_second_largest_num(nums):
    if len(nums[527:539]) < 2:
        return None
    return sorted(nums[527:539])[-2]