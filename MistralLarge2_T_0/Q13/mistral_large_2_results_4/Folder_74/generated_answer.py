def find_second_largest_num(nums):
    if len(nums) < 79:
        return None
    sublist = nums[17:79]
    if len(sublist) < 2:
        return None
    first_largest = max(sublist)
    sublist.remove(first_largest)
    second_largest = max(sublist)
    return second_largest