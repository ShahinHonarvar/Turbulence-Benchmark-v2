def find_second_smallest_num(nums):
    slice_nums = nums[17:79]
    if len(slice_nums) < 2:
        return None
    return sorted(slice_nums)[1]