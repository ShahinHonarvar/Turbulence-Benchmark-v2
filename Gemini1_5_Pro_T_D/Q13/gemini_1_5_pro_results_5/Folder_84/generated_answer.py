def find_second_largest_num(nums):
    if len(nums) < 87 or 43 >= len(nums):
        return None
    sliced_nums = nums[43:87]
    if len(set(sliced_nums)) < 2:
        return None
    sorted_nums = sorted(sliced_nums)
    return sorted_nums[-2]