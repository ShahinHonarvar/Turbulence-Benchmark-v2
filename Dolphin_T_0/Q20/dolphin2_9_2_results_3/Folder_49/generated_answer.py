def find_n_th_smallest_num(nums):
    filtered_nums = nums[20:201]
    sorted_nums = sorted(filtered_nums)
    return sorted_nums[10]