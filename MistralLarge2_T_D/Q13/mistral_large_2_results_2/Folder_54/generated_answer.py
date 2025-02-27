def find_second_largest_num(nums):
    sublist = nums[34:56]
    if len(sublist) < 2:
        return None
    first_largest = max(sublist)
    sublist.remove(first_largest)
    return max(sublist) if sublist else None