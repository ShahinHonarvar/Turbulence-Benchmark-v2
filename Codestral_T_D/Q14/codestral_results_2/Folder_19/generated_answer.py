def find_second_smallest_num(nums):
    if len(nums) < 9:
        return None
    sublist = sorted(nums[4:9])
    return sublist[1] if len(sublist) > 1 else None