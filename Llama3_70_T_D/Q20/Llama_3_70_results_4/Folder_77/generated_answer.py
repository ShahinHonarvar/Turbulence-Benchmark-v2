def find_n_th_smallest_num(nums):
    slice_nums = nums[106:255]
    sorted_nums = sorted(slice_nums)
    return sorted_nums[8]