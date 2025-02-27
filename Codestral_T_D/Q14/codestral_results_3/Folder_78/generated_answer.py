def find_second_smallest_num(nums):
    if 17 <= len(nums) <= 78:
        sublist = sorted(nums[17:79])
        return sublist[1] if len(sublist) > 1 else None
    else:
        return None