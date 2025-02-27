def find_second_largest_num(nums):
    if len(nums) < 606:
        return None
    sliced_nums = nums[533:606]
    if len(set(sliced_nums)) < 2:
        return None
    sorted_nums = sorted(sliced_nums)
    return sorted_nums[-2]