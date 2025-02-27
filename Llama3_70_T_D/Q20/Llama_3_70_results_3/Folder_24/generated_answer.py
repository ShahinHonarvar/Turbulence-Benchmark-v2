def find_n_th_smallest_num(nums):
    n = 6
    start = 43
    end = 80
    return sorted(nums[start:end + 1])[n - 1]