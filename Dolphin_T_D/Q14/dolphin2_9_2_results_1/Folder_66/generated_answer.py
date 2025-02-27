def find_second_smallest_num(nums):
    sublist = nums[62:100]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[1] if sublist[1] != sublist[0] else None