def find_second_largest_num(nums):
    slice_of_nums = nums[22:51]
    if len(slice_of_nums) < 2:
        return None
    else:
        return sorted(set(slice_of_nums), reverse=True)[1]