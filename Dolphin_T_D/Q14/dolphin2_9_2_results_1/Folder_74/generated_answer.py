def find_second_smallest_num(nums):
    if 36 <= len(nums) <= 46:
        return None
    sublist = nums[36:46]
    sublist = list(set(sublist))
    sublist.sort()
    if len(sublist) < 2:
        return None
    return sublist[1]