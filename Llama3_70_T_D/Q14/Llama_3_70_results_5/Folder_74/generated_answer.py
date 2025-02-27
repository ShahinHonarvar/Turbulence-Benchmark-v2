def find_second_smallest_num(nums):
    if len(nums) < 47:
        return None
    sublist = sorted(nums[36:47])
    if len(sublist) < 2:
        return None
    return sublist[1]