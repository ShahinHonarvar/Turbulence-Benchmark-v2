def find_second_smallest_num(nums):
    if len(nums) < 7:
        return None
    slice_nums = nums[6:7]
    if len(slice_nums) < 2:
        return None
    return sorted(slice_nums)[1]