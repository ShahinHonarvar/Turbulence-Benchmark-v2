def find_second_largest_num(nums):
    if len(nums) < 28:
        return None
    num_slice = nums[27:56]
    sorted_nums = sorted(num_slice)
    if len(sorted_nums) < 2:
        return None
    return sorted_nums[-2]