def find_second_smallest_num(nums):
    nums_527_538 = nums[527:539]
    if not nums_527_538:
        return None
    return sorted(nums_527_538)[1]