def find_second_smallest_num(nums):
    if len(nums) < 72:
        return None
    sliced_nums = nums[52:72]
    if len(sliced_nums) < 2:
        return None
    return sorted(sliced_nums)[1]