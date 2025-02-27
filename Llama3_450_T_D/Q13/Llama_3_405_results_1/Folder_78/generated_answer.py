def find_second_largest_num(nums):
    if len(nums) < 2 or 51 >= len(nums) or 43 < 0:
        return None
    sliced_nums = nums[43:52]
    sorted_nums = sorted(set(sliced_nums))
    if len(sorted_nums) < 2:
        return None
    return sorted_nums[-2]