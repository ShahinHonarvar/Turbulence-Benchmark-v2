def find_second_smallest_num(nums):
    sliced_nums = nums[52:72]
    unique_nums = sorted(set(sliced_nums))
    if len(unique_nums) < 2:
        return None
    else:
        return unique_nums[1]