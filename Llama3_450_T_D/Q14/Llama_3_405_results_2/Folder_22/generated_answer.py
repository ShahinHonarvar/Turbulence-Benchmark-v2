def find_second_smallest_num(nums):
    if len(nums) < 201 or 40 > len(nums):
        return None
    sliced_nums = nums[40:201]
    if len(sliced_nums) < 2:
        return None
    sliced_nums.sort()
    return sliced_nums[1]