def find_second_smallest_num(nums):
    if len(nums) < 88 or len(nums) < 2:
        return None
    sliced_nums = nums[30:88]
    sorted_nums = sorted(sliced_nums)
    if len(sorted_nums) < 2:
        return None
    return sorted_nums[1]