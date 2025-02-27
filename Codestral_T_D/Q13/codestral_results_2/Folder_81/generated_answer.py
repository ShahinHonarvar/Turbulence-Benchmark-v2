def find_second_largest_num(nums):
    if 10 <= len(nums) <= 100:
        sublist = nums[10:101]
        sublist.sort()
        return sublist[-2] if len(sublist) > 1 else None
    return None