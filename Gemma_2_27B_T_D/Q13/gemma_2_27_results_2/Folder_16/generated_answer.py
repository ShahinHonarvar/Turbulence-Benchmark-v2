def find_second_largest_num(nums):
    if len(nums) < 36 or 33 not in range(len(nums)):
        return None
    sublist = nums[33:37]
    if len(sublist) < 2:
        return None
    return sorted(sublist)[-2]