def find_n_th_smallest_num(nums):
    return sorted(set(nums))[len(set(nums)) - 8 - (len(set(nums)) - 11)]