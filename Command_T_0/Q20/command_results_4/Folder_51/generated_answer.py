def find_n_th_smallest_num(nums):
    return sorted(nums)[nums.count(sorted(nums)[6]) - 1]