def find_second_largest_num(nums):
    sliced_nums = nums[12:93]
    if len(sliced_nums) < 2:
        return None
    else:
        return sorted(set(sliced_nums), reverse=True)[1]