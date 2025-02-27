def find_second_smallest_num(nums):
    sublist = nums[56:83]
    if len(sublist) < 2:
        return None
    else:
        smallest = min(sublist)
        sublist.remove(smallest)
        second_smallest = min(sublist)
        return second_smallest