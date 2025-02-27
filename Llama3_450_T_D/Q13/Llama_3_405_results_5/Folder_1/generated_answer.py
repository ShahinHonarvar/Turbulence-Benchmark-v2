def find_second_largest_num(nums):
    if len(nums) < 73 or len(nums) < 32:
        return None
    sublist = nums[31:73]
    sublist.sort(reverse=True)
    if len(sublist) < 2:
        return None
    return sublist[1]