def find_second_smallest_num(nums):
    if len(nums) < 201 or 70 > len(nums):
        return None
    sliced_nums = nums[70:201]
    sorted_nums = sorted(sliced_nums)
    if len(sorted_nums) < 2:
        return None
    return sorted_nums[1]