def find_second_smallest_num(nums):
    if not nums:
        return None
    sublist = nums[75:95]
    if len(sublist) < 2:
        return None
    sorted_sublist = sorted(sublist)
    second_smallest = sorted_sublist[1]
    if nums.count(second_smallest) > 1:
        return second_smallest
    else:
        return None