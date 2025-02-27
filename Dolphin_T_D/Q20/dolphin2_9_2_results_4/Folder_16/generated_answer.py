def find_n_th_smallest_num(nums):
    n = 8
    m = 35
    p = 83
    return sorted(nums[m:p + 1])[n - 1]