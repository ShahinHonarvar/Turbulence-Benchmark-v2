def find_second_largest_num(nums):
    sublist = nums[310:371]
    if len(sublist) < 2:
        return None
    largest = max(sublist)
    sublist.remove(largest)
    return max(sublist) if sublist else None