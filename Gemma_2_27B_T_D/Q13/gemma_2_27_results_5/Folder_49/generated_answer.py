def find_second_largest_num(nums):
    sliced_nums = nums[80:201]
    if len(sliced_nums) < 2:
        return None
    sorted_nums = sorted(sliced_nums)
    return sorted_nums[-2]