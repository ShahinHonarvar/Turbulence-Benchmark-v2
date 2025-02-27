def find_second_smallest_num(nums):
    if len(nums) < 538 - 527 + 1:
        return None
    sublist = nums[527:539]
    sublist.sort()
    if len(sublist) < 2:
        return None
    return sublist[1]