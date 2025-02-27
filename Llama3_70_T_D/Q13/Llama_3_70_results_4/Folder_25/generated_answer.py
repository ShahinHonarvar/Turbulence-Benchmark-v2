def find_second_largest_num(nums):
    sliced_nums = nums[29:94]
    if len(sliced_nums) < 2:
        return None
    return sorted(set(sliced_nums), reverse=True)[1]