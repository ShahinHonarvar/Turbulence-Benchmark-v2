def find_second_smallest_num(nums):
    if not nums or len(nums) < 30:
        return None
    sublist = sorted(nums[29:80])
    if len(sublist) < 2:
        return None
    return sublist[1]