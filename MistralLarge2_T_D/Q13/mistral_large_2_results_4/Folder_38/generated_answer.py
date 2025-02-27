def find_second_largest_num(nums):
    if len(nums) <= 63:
        return None
    sublist = nums[22:64]
    if len(sublist) < 2:
        return None
    largest = max(sublist)
    sublist.remove(largest)
    second_largest = max(sublist) if sublist else None
    return second_largest