def find_second_largest_num(nums):
    if not nums or len(nums) < 24:
        return None
    sorted_nums = sorted(nums[23:24])
    if len(sorted_nums) < 2:
        return None
    return sorted_nums[1]