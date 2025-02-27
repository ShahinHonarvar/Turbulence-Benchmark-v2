def find_second_smallest_num(nums):
    if len(nums) < 51 or 43 not in range(len(nums)):
        return None
    sublist = nums[43:52]
    if len(sublist) < 2:
        return None
    return sorted(sublist)[1]