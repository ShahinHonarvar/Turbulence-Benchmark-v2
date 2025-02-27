def find_second_smallest_num(nums):
    if 200 < len(nums) < 30:
        return None
    sublist = nums[30:201]
    if len(sublist) < 2:
        return None
    sublist.sort()
    for i in range(1, len(sublist)):
        if sublist[i] != sublist[i - 1]:
            return sublist[i]
    return None