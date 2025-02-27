def find_second_largest_num(nums):
    if len(nums[639:976]) < 2:
        return None
    return sorted(nums[639:976])[-2]