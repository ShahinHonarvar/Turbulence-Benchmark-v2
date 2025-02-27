def find_second_largest_num(nums):
    if len(nums) < 65:
        return None
    sublist = nums[14:65]
    if len(sublist) < 2:
        return None
    first_largest = max(sublist)
    sublist.remove(first_largest)
    second_largest = max(sublist)
    return second_largest