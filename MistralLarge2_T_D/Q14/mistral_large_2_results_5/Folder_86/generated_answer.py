def find_second_smallest_num(nums):
    sublist = nums[33:37]
    if len(sublist) < 2:
        return None
    unique_nums = set(sublist)
    if len(unique_nums) < 2:
        return None
    sorted_nums = sorted(unique_nums)
    return sorted_nums[1]