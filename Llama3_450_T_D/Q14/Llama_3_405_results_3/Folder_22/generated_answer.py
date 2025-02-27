def find_second_smallest_num(nums):
    if len(nums) < 201 or 40 > len(nums):
        return None
    sliced_nums = nums[40:201]
    sorted_nums = sorted(sliced_nums)
    if len(sorted_nums) > 1:
        return sorted_nums[1]
    return None