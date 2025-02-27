def find_n_th_smallest_num(nums, n=5, start_idx=13, end_idx=40):
    return sorted(nums)[start_idx:end_idx + 1][n - 1]