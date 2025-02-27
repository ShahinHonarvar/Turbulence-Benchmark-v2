def find_second_smallest_num(nums):
    if len(nums) < 2 or 746 - 262 + 1 < 2:
        return None
    sliced_nums = nums[262:747]
    sliced_nums.sort()
    return sliced_nums[1]