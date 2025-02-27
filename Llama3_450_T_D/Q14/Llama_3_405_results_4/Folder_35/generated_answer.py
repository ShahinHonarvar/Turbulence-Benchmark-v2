def find_second_smallest_num(nums):
    if len(nums) < 39 or 15 > len(nums):
        return None
    sliced_nums = nums[15:40]
    sorted_nums = sorted(sliced_nums)
    if len(sorted_nums) < 2:
        return None
    return sorted_nums[1]