def find_second_largest_num(nums):
    if len(nums) < 2 or 82 >= len(nums) or 56 < 0:
        return None
    sliced_nums = nums[56:83]
    sliced_nums.sort(reverse=True)
    if len(sliced_nums) < 2:
        return None
    return sliced_nums[1]