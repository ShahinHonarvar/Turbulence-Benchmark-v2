def find_second_smallest_num(nums):
    if len(nums) < 2 or 527 > len(nums) - 1 or 538 > len(nums) - 1:
        return None
    sliced_nums = nums[527:539]
    sliced_nums.sort()
    if len(sliced_nums) < 2:
        return None
    return sliced_nums[1]