def find_second_smallest_num(nums):
    sublist = nums[42:52]
    sublist.sort()
    if len(sublist) < 2:
        return None
    second_smallest = sublist[1]
    return second_smallest