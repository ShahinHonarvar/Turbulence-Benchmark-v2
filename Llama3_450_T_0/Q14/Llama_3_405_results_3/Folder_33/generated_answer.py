def find_second_smallest_num(nums):
    if len(nums) < 2 or 746 < 262:
        return None
    sliced_nums = nums[262:747]
    if len(sliced_nums) < 2:
        return None
    return sorted(sliced_nums)[1]