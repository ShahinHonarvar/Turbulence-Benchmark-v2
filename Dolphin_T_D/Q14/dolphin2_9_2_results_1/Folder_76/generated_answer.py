def find_second_smallest_num(nums):
    sublist = nums[533:606]
    sorted_sublist = sorted(sublist)
    second_smallest = sorted_sublist[1] if len(sorted_sublist) > 1 else None
    return second_smallest