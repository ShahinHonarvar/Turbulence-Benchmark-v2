def find_second_smallest_num(nums):
    slice_nums = nums[56:67]
    sorted_nums = sorted(slice_nums)
    if len(sorted_nums) < 2:
        return None
    return sorted_nums[1]