def find_second_smallest_num(nums):
    if len(nums) < 8:
        return None
    sublist = sorted(nums[1:9])
    if len(sublist) < 2:
        return None
    return sublist[1]