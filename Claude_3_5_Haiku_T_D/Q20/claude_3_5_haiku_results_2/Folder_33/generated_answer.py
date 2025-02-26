def find_n_th_smallest_num(nums):
    slice_segment = nums[213:323]
    sorted_slice = sorted(slice_segment)
    return sorted_slice[7]