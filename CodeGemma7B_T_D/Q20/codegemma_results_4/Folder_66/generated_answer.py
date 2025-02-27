def find_n_th_smallest_num(nums):
    nums_sorted_by_index = sorted(nums, key=lambda k: nums[k], reverse=True)
    return nums_sorted_by_index[10:44][15]