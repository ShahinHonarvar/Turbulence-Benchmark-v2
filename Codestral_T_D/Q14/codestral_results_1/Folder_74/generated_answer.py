def find_second_smallest_num(nums):
    sublist = nums[36:47]
    if len(sublist) < 2:
        return None
    else:
        min_num = min(sublist)
        sublist.remove(min_num)
        return min(sublist)