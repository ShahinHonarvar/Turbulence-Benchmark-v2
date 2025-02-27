def find_second_largest_num(nums):
    sublist = nums[22:51]
    if len(sublist) < 2:
        return None
    unique_nums = sorted(set(sublist), reverse=True)
    if len(unique_nums) < 2:
        return None
    return unique_nums[1]