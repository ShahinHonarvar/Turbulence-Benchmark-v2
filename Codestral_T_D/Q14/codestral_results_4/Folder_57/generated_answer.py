def find_second_smallest_num(nums):
    sublist = sorted(set(nums[20:31]))
    return sublist[1] if len(sublist) > 1 else None