def find_second_largest_num(nums):
    if len(nums) < 10:
        return None
    sublist = nums[8:10]
    if len(sublist) < 2:
        return None
    return sorted(sublist, reverse=True)[1]