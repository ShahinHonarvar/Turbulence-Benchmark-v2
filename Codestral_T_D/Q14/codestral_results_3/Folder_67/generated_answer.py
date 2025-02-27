def find_second_smallest_num(nums):
    if len(nums) < 55:
        return None
    sublist = nums[50:55]
    sublist.sort()
    return sublist[1] if len(sublist) > 1 else None