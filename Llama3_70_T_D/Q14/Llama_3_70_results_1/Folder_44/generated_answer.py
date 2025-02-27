def find_second_smallest_num(nums):
    slice_nums = nums[91:100]
    if len(slice_nums) < 2:
        return None
    return sorted(set(slice_nums))[1]