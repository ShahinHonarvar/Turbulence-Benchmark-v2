def find_second_smallest_num(nums):
    sublist = nums[28:41]
    if len(sublist) < 2:
        return None
    else:
        smallest = min(sublist)
        sublist.remove(smallest)
        return min(sublist)