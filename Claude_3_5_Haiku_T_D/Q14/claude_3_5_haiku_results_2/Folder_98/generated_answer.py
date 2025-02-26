def find_second_smallest_num(nums):
    if len(nums) <= 6:
        return None
    slice_list = nums[6:7]
    if not slice_list:
        return None
    return slice_list[0]