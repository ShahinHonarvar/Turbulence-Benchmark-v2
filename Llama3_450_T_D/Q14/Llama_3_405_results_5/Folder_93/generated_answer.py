def find_second_smallest_num(nums):
    if len(nums) < 89 or len(nums) <= 75:
        return None
    sliced_nums = nums[75:89]
    sorted_nums = sorted(sliced_nums)
    if len(sorted_nums) < 2:
        return None
    return sorted_nums[1]