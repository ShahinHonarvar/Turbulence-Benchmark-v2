def find_second_smallest_num(nums):
    if len(nums) <= 4:
        return None
    sublist = nums[4:5]
    if not sublist:
        return None
    return sublist[0]