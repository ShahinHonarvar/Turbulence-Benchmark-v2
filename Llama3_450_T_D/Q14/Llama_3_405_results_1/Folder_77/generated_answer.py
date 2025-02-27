def find_second_smallest_num(nums):
    if len(nums) < 2 or 639 >= len(nums) or 975 < 639:
        return None
    sliced_nums = nums[639:976]
    sliced_nums.sort()
    if len(sliced_nums) < 2:
        return None
    return sliced_nums[1]