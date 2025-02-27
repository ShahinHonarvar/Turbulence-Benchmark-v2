def find_second_largest_num(nums):
    if not nums:
        return None
    if len(nums) < 20:
        return None
    sublist = nums[52:72]
    sublist.sort()
    return sublist[-2] if len(sublist) >= 2 else None