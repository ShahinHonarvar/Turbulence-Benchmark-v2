def find_second_largest_num(nums):
    if len(nums) < 83:
        return None
    sublist = nums[56:83]
    if len(sublist) < 2:
        return None
    unique_nums = sorted(set(sublist), reverse=True)
    if len(unique_nums) < 2:
        return None
    return unique_nums[1]