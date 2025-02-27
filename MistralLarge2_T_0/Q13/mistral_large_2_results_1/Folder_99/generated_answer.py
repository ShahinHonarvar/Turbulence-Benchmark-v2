def find_second_largest_num(nums):
    if len(nums) < 371:
        return None
    sublist = nums[310:371]
    if len(sublist) < 2:
        return None
    first_largest = max(sublist)
    sublist.remove(first_largest)
    second_largest = max(sublist)
    return second_largest