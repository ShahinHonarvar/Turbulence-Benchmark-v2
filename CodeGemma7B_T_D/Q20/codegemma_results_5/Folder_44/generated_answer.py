def find_n_th_smallest_num(nums, n, start_index, end_index):
    return sorted(nums[start_index:end_index + 1])[n - 1]