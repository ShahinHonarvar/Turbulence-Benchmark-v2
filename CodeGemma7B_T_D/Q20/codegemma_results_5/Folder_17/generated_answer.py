def find_n_th_smallest_num(nums, start, end, n):
    sorted_nums = sorted(nums[start:end + 1])
    return sorted_nums[n - 1]