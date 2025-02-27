def find_second_smallest_num(nums):
    sublist = nums[65:94]
    if len(set(sublist)) < 2:
        return None
    else:
        return sorted(sublist)[1]