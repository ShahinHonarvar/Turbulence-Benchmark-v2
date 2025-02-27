def find_second_largest_num(nums):
    if len(nums[34:56]) < 2:
        return None
    sorted_nums = sorted(nums[34:56])
    return sorted_nums[-2]