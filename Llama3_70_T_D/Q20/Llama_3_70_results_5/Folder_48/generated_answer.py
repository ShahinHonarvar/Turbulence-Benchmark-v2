def find_n_th_smallest_num(nums):
    n = 10
    start = 127
    end = 848
    return sorted(nums[start:end + 1])[n - 1]