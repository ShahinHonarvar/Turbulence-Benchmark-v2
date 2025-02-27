def find_second_largest_num(nums):
    nums_slice = nums[639:976]
    sorted_nums = sorted(nums_slice)
    if len(sorted_nums) > 1:
        return sorted_nums[-2]
    else:
        return None