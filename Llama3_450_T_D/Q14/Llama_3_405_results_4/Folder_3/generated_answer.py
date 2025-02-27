def find_second_smallest_num(nums):
    if len(nums) < 55 or 27 > len(nums):
        return None
    sliced_nums = nums[27:56]
    sliced_nums.sort()
    if len(sliced_nums) < 2:
        return None
    return sliced_nums[1]