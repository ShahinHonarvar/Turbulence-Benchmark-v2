def find_second_smallest_num(nums):
    if len(nums) < 98:
        return None
    sliced_nums = nums[21:98]
    sorted_nums = sorted(sliced_nums)
    if len(sorted_nums) < 2:
        return None
    return sorted_nums[1]