def find_n_th_smallest_num(nums):
    subset = nums[106:255]
    subset.sort()
    return subset[8]