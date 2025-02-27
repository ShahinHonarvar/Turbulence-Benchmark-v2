def find_second_smallest_num(nums):
    if len(nums) < 40:
        return None
    sliced_nums = nums[15:40]
    sliced_nums.sort()
    if len(sliced_nums) < 2:
        return None
    return sliced_nums[1]