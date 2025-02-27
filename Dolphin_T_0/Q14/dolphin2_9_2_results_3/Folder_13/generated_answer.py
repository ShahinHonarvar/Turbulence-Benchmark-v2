def find_second_smallest_num(nums):
    if len(nums) < 33:
        return None
    sublist = nums[28:33]
    sublist.sort()
    for i in range(len(sublist) - 1):
        if sublist[i] != sublist[0]:
            return sublist[i]
    return None