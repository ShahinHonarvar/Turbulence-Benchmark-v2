def find_second_smallest_num(nums):
    sublist = nums[59:98]
    sublist.sort()
    return sublist[1] if len(sublist) > 1 else None