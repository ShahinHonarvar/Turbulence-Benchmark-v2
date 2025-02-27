def find_second_largest_num(nums):
    if len(nums) < 9:
        return None
    sliced_nums = nums[1:9]
    sliced_nums = list(set(sliced_nums))
    if len(sliced_nums) < 2:
        return None
    sliced_nums.sort(reverse=True)
    return sliced_nums[1]