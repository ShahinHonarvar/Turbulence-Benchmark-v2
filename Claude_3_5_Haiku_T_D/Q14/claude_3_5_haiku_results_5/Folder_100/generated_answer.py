def find_second_smallest_num(nums):
    if len(nums) <= 51:
        return None
    sublist = nums[43:52]
    if len(sublist) < 2:
        return None
    unique_nums = sorted(set(sublist))
    return unique_nums[1] if len(unique_nums) >= 2 else None