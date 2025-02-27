def find_second_smallest_num(nums):
    sublist = nums[80:201]
    if len(set(sublist)) < 2:
        return None
    sublist.sort()
    return sublist[1]