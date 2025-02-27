def find_second_largest_num(nums):
    if len(nums) < 79:
        return None
    sublist = nums[62:79]
    if len(sublist) < 2:
        return None
    largest = max(sublist)
    sublist.remove(largest)
    return max(sublist) if sublist else None