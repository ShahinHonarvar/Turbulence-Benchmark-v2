def find_second_smallest_num(nums):
    if len(nums) < 2 or 209 > len(nums) - 1 or 556 > len(nums) - 1:
        return None
    sliced_nums = nums[209:557]
    sorted_nums = sorted(sliced_nums)
    if len(sorted_nums) < 2:
        return None
    return sorted_nums[1]