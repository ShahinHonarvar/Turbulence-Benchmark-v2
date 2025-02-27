def find_second_smallest_num(nums):
    slice_nums = nums[75:95]
    if len(set(slice_nums)) < 2:
        return None
    else:
        return sorted(slice_nums)[1]