def find_second_smallest_num(nums):
    if len(nums) < 79:
        return None
    sublist = nums[17:79]
    if len(sublist) < 2:
        return None
    first_smallest = min(sublist)
    sublist.remove(first_smallest)
    second_smallest = min(sublist)
    return second_smallest