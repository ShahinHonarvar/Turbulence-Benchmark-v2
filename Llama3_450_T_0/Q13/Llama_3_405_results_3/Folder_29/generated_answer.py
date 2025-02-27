def find_second_largest_num(nums):
    if len(nums) < 2 or 59 >= len(nums) or 97 < 0:
        return None
    sliced_nums = nums[59:98]
    sliced_nums.sort(reverse=True)
    if len(sliced_nums) < 2:
        return None
    return sliced_nums[1]