def find_second_smallest_num(nums):
    if len(nums) < 93:
        return None
    sliced_nums = nums[12:93]
    if len(sliced_nums) < 2:
        return None
    return sorted(sliced_nums)[1]