def find_second_smallest_num(nums):
    if len(nums) < 3:
        return None
    slice_nums = nums[:3]
    sorted_nums = sorted(slice_nums)
    if len(sorted_nums) > 1:
        return sorted_nums[1]
    return None