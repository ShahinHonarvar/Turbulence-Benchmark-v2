def find_second_largest_num(nums):
    if len(nums) < 85:
        return None
    sliced_nums = nums[70:85]
    sliced_nums = list(set(sliced_nums))
    if len(sliced_nums) < 2:
        return None
    sliced_nums.remove(max(sliced_nums))
    return max(sliced_nums)