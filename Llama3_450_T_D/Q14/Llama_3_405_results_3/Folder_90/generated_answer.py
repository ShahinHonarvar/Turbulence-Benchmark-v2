def find_second_smallest_num(nums):
    nums_sliced = nums[527:539]
    if len(nums_sliced) < 2:
        return None
    return sorted(nums_sliced)[1]