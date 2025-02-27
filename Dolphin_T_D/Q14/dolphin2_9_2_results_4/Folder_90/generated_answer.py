def find_second_smallest_num(nums):
    if 527 <= 538 < len(nums):
        sublist = nums[527:539]
        sublist.sort()
        if len(sublist) > 1:
            return sublist[1]
    return None