def find_second_largest_num(nums):
    if len(nums[17:79]) < 2:
        return None
    return sorted(nums[17:79])[-2]