def find_second_smallest_num(nums):
    sublist = nums[661:925]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[1]