def find_second_smallest_num(nums):
    slice_of_nums = nums[37:77]
    if len(slice_of_nums) < 2:
        return None
    else:
        return sorted(slice_of_nums)[1]