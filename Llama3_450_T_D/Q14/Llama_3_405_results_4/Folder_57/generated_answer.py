def find_second_smallest_num(nums):
    sliced_nums = nums[20:31]
    if len(sliced_nums) < 2:
        return None
    sorted_nums = sorted(sliced_nums)
    return sorted_nums[1]