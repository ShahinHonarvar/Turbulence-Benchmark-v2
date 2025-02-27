def find_second_smallest_num(nums):
    if len(nums) <= 4:
        return None
    sublist = nums[4:5]
    if len(sublist) < 2:
        return None
    first_min = min(sublist)
    sublist.remove(first_min)
    second_min = min(sublist)
    return second_min