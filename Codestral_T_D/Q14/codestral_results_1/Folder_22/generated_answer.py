def find_second_smallest_num(nums):
    if 40 <= len(nums) <= 200:
        sublist = sorted(nums[40:201])
        return sublist[1] if len(sublist) > 1 else None
    return None