def find_second_smallest_num(nums):
    sublist = nums[40:81]
    if len(sublist) < 2:
        return None
    sorted_sublist = sorted(sublist)
    return sorted_sublist[1]