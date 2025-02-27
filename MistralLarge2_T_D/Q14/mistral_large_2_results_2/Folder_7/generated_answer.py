def find_second_smallest_num(nums):
    sublist = nums[686:988]
    if len(sublist) < 2:
        return None
    first_smallest = min(sublist)
    sublist.remove(first_smallest)
    return min(sublist)