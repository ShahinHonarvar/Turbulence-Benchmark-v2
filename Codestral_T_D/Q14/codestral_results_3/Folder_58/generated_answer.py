def find_second_smallest_num(nums):
    sublist = sorted(nums[310:371])
    if len(sublist) < 2:
        return None
    return sublist[1]