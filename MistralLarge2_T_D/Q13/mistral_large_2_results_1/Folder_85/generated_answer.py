def find_second_largest_num(nums):
    if len(nums) < 9:
        return None
    sublist = sorted(nums[6:9], reverse=True)
    if len(sublist) < 2:
        return None
    return sublist[1]