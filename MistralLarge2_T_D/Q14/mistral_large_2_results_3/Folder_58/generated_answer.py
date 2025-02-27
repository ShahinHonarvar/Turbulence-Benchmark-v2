def find_second_smallest_num(nums):
    sublist = nums[310:371]
    if len(sublist) < 2:
        return None
    first_smallest = min(sublist)
    sublist.remove(first_smallest)
    return min(sublist) if sublist else None