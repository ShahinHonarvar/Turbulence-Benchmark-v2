def find_second_largest_num(nums):
    if len(nums) < 209 or len(nums) < 556:
        return None
    sliced_nums = nums[209:557]
    sliced_nums.sort(reverse=True)
    if len(sliced_nums) < 2:
        return None
    return sliced_nums[1]