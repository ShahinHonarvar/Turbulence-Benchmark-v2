def find_second_largest_num(nums):
    if len(nums) < 50:
        return None
    sliced_nums = nums[35:50]
    sliced_nums.sort(reverse=True)
    if len(sliced_nums) > 1:
        return sliced_nums[1]
    return None