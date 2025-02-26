def find_second_smallest_num(nums):
    if len(nums) < 11:
        return None
    sublist = nums[10:11]
    if not sublist:
        return None
    return min(sublist)