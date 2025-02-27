def find_second_smallest_num(nums):
    if len(nums) < 201 or 40 > len(nums):
        return None
    sliced_nums = nums[40:201]
    sliced_nums.sort()
    if len(sliced_nums) > 1:
        return sliced_nums[1]
    else:
        return None