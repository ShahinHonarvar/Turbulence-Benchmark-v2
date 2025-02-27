def find_second_smallest_num(nums):
    if len(nums) < 78:
        return None
    slice_nums = nums[66:78]
    sorted_nums = sorted(slice_nums)
    if len(sorted_nums) < 2:
        return None
    return sorted_nums[1]