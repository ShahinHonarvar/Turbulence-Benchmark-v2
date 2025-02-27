def find_second_smallest_num(nums):
    slice_nums = nums[8:10]
    if len(slice_nums) < 2:
        return None
    else:
        return sorted(slice_nums)[1]